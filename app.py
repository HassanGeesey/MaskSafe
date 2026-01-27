import os
import threading
import time
from flask import Flask, render_template, Response, request, redirect, url_for, send_from_directory, jsonify
import cv2
import numpy as np
from camera import VideoCamera
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS_IMG = {'png', 'jpg', 'jpeg'}
ALLOWED_EXTENSIONS_VID = {'mp4', 'avi', 'mov'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize camera logic once
camera_processor = VideoCamera()

# Global dictionary to store progress: {filename: percentage}
video_progress = {}

def allowed_file(filename, extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in extensions

def gen_frames():
    # Use cv2.CAP_DSHOW for Windows to avoid potential backend issues (grey screen/slow load)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        success, frame = cap.read()
        if not success:
            break
        
        try:
            processed_frame = camera_processor.get_frame(frame)
            ret, buffer = cv2.imencode('.jpg', processed_frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except Exception as e:
            print(f"Error processing frame: {e}")
            break
            
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live')
def live():
    return render_template('live.html')

@app.route('/metrics')
def metrics():
    return render_template('metrics.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename, ALLOWED_EXTENSIONS_IMG):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Process Image
            img = cv2.imread(filepath)
            processed_img = camera_processor.get_frame(img)
            
            # Save processed image
            processed_filename = 'processed_' + filename
            processed_filepath = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
            cv2.imwrite(processed_filepath, processed_img)
            
            return render_template('upload_image.html', uploaded_image=processed_filename)
            
    return render_template('upload_image.html')

def process_video_thread(filepath, filename):
    global video_progress
    try:
        cap = cv2.VideoCapture(filepath)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        processed_filename = 'processed_' + filename
        processed_filepath = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
        
        # Try H.264 (avc1) for better browser compatibility
        fourcc = cv2.VideoWriter_fourcc(*'avc1') 
        out = cv2.VideoWriter(processed_filepath, fourcc, fps, (width, height))
        
        # Fallback if avc1 fails to initialize (writer not opened)
        if not out.isOpened():
             print("avc1 failed, falling back to mp4v")
             fourcc = cv2.VideoWriter_fourcc(*'mp4v')
             out = cv2.VideoWriter(processed_filepath, fourcc, fps, (width, height))
        
        current_frame = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            processed_frame = camera_processor.get_frame(frame)
            out.write(processed_frame)
            
            current_frame += 1
            if total_frames > 0:
                progress = int((current_frame / total_frames) * 100)
                video_progress[filename] = progress
        
        cap.release()
        out.release()
        video_progress[filename] = 100 # Ensure it hits 100
        
    except Exception as e:
        print(f"Error processing video: {e}")
        video_progress[filename] = -1 # Error state

@app.route('/upload_video', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename, ALLOWED_EXTENSIONS_VID):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Start background thread
            video_progress[filename] = 0
            thread = threading.Thread(target=process_video_thread, args=(filepath, filename))
            thread.start()
            
            return render_template('upload_video.html', processing_filename=filename)

    return render_template('upload_video.html')

@app.route('/progress/<filename>')
def progress(filename):
    global video_progress
    return jsonify({'progress': video_progress.get(filename, 0)})

@app.route('/result_video/<filename>')
def result_video(filename):
     processed_filename = 'processed_' + filename
     return render_template('upload_video.html', uploaded_video=processed_filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
