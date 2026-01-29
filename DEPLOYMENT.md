# Deploying MaskSafe to the Internet (FREE)

## ⚠️ Important Notes

**Webcam/Camera Access:** The live camera feed feature will NOT work on deployed web apps because browsers require HTTPS and specific permissions. However, image and video upload features will work perfectly!

**Large Model Files:** Your YOLO weights files (~240MB) are too large for Git. You'll need to handle them specially.

---

## Option 1: Render (Recommended - Easiest)

### Steps:

1. **Push updates to GitHub:**
```bash
git add .
git commit -m "Add deployment configuration"
git push origin main
```

2. **Create a Render account:**
   - Go to https://render.com
   - Sign up with your GitHub account (free)

3. **Create a new Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository (MaskSafe)
   - Configure:
     - **Name:** masksafe
     - **Environment:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`
     - **Plan:** Free

4. **Upload weight files after deployment:**
   Since weight files are too large for Git, you have two options:
   
   **Option A:** Use a file hosting service (Google Drive, Dropbox) and download on startup
   
   **Option B:** Upload directly via Render Shell:
   - After deployment, go to your service → Shell tab
   - Upload files manually (up to 512MB supported)

5. **Deploy:**
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment
   - Your app will be live at `https://masksafe.onrender.com`

### Limitations:
- Free tier sleeps after 15 min of inactivity
- Live camera feed won't work (browser security)
- Need to upload weight files separately

---

## Option 2: Hugging Face Spaces (Best for ML Models)

### Steps:

1. **Create account:**
   - Go to https://huggingface.co
   - Sign up (free)

2. **Create a new Space:**
   - Click your profile → "New Space"
   - Name: `MaskSafe`
   - SDK: **Gradio** or **Streamlit**
   - Visibility: Public

3. **Important:** You'll need to rewrite the app using Gradio or Streamlit instead of Flask. Would you like me to help with this?

### Advantages:
- Designed for ML models
- Handles large files with Git LFS
- Always-on (no sleeping)
- Great for sharing AI projects

---

## Option 3: Railway

### Steps:

1. **Push to GitHub** (if not done)

2. **Create Railway account:**
   - Go to https://railway.app
   - Sign up with GitHub

3. **Deploy:**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select MaskSafe
   - Railway auto-detects Python and uses your Procfile

4. **Add weight files:**
   - Use Railway's volume storage or external hosting

### Free tier:
- $5 free credit per month
- Sufficient for light usage

---

## Recommended Solution

For **MaskSafe**, I recommend:

1. **For quick demo:** Use **Render** - Upload only image/video features
2. **For full ML showcase:** Convert to **Gradio** on **Hugging Face Spaces**

**Note:** The live webcam feature requires running locally due to browser security restrictions (HTTPS + camera permissions).

---

## What would you like to do?

1. Deploy to Render now (image/video features only)
2. Convert to Gradio for Hugging Face Spaces (full features + ML showcase)
3. Deploy to Railway

Let me know and I'll help you proceed!
