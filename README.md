# MaskSafe

AI-powered real-time face mask detection system using YOLOv3 with a modern web interface.

## Features

- **Live Camera Feed**: Real-time mask detection via webcam
- **Image Upload**: Analyze uploaded images for mask compliance
- **Video Processing**: Process and analyze videos with progress tracking
- **Model Metrics**: View detailed performance statistics
- **Modern UI**: Clean, minimal, and responsive interface

## Model Performance

- **mAP (0.50)**: 94.04%
- **F1-Score**: 0.92
- **Architecture**: YOLOv3 with Darknet-53 backbone

### Class-wise Performance
- Mask: 96.96% AP
- Improperly Masked: 92.80% AP
- No Mask: 92.37% AP

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/MaskSafe.git
cd MaskSafe
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Download the pre-trained weights:
   - Place `yolov3_mask_last.weights` in the project root
   - Place `darknet53.conv.74` in the project root

## Quick Start

**Windows:** Simply double-click `start.bat`

**Mac/Linux:** Run `./start.sh` (make executable first: `chmod +x start.sh`)

**Manual:**
```bash
python app.py
```

Then open your browser and navigate to: `http://127.0.0.1:5000`

## Project Structure

```
anti/
├── app.py                 # Flask application
├── camera.py              # Video processing logic
├── detect_mask.cfg        # YOLOv3 configuration
├── mask.names             # Class labels
├── requirements.txt       # Python dependencies
├── static/
│   ├── style.css         # Modern UI styles
│   └── uploads/          # Uploaded files (gitignored)
└── templates/
    ├── index.html        # Home page
    ├── live.html         # Live feed
    ├── upload_image.html # Image upload
    ├── upload_video.html # Video upload
    └── metrics.html      # Model metrics
```

## Technologies Used

- **Backend**: Flask, OpenCV, NumPy
- **Frontend**: HTML, CSS, JavaScript, Font Awesome
- **Model**: YOLOv3 (Darknet)
- **Libraries**: opencv-python, Flask, Werkzeug

## Usage

### Live Detection
Navigate to `/live` to start real-time mask detection using your webcam.

### Image Analysis
Upload an image at `/upload_image` to analyze mask compliance.

### Video Processing
Upload a video at `/upload_video` and watch the progress bar as frames are processed.

### Model Metrics
View detailed performance metrics at `/metrics`.

## Model Details

The YOLOv3 model is trained to detect three classes:
1. **mask** - Person wearing a mask correctly
2. **improperly** - Person wearing a mask incorrectly
3. **no mask** - Person not wearing a mask

## Requirements

- Python 3.7+
- Webcam (for live detection)
- YOLO weights files (see Installation)

## License

This project is for educational purposes.

## Credits

Model trained using the Face Mask Detection YOLO dataset.
