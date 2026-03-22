# 🐄 Intelligent Cattle Breed Classifier

An AI-powered web application that accurately identifies the breed of cattle from an uploaded image using Deep Learning.

## ✨ Features
- **Deep Learning Core**: Built on a highly-optimized `EfficientNetV2-S` architecture using PyTorch.
- **Professional Web UI**: Fully responsive, theme-aware modern Streamlit interface with animations.
- **Confidence Tracking**: Calculates explicit probability scores (0% to 100%) and displays a stylish progress bar breakdown for the Top 5 most likely breeds.
- **Smart Rejection**: Automatically rejects non-cattle images (like dogs, objects, or monkeys) to prevent false predictions if the AI's confidence score falls under our strict 65% threshold.

<br>

## 🚀 How to Run the App

### 1. Prerequisites
Ensure you have Python installed, then install all required libraries using `pip`:
```bash
pip install -r requirements.txt
```

*(Note: The `requirements.txt` should contain `torch`, `torchvision`, `streamlit`, and `Pillow` at a minimum)*

### 2. Launching the Application Safely
Because Windows environments often have overlapping Python versions or failing `streamlit` global path links, you should **always use the provided `run.bat` file** to launch the environment cleanly.

1. Open your terminal or file explorer and navigate to this folder.
2. Double-click the **`run.bat`** file (or type `.\run.bat` in your Command Prompt/PowerShell).
3. The AI server will spin up and open automatically in your browser at `http://localhost:8501`.

### 3. Usage
- Simply drag and drop (or select) a photograph of a cattle format (`.jpg`, `.jpeg`, `.png`).
- The system natively catches transparent PNGs/RGBA issues and cleans them.
- Wait a split second while the neural network analyzes the anatomical features.
- Review your primary prediction card and the comprehensive Top 5 breakdown!

<br>

## 📁 Core Structure
- `app.py` - The core application interface handling uploads, UX design, and layout.
- `model/` - Contains the custom `model.py` PyTorch structure mapped strictly to your incoming `.pth` weight files.
- `utils/` - Contains `labels.json` for all breed classes, and the image transformation architecture.
- `run.bat` - The automated script that prevents `ModuleNotFoundError` by forcing execution through the correct environment.
