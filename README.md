# 🐄 AI Cattle Breed Classifier

A modern, deep learning-powered web application for identifying cattle breeds from images. Built with **Flask** and **PyTorch**, this system uses the **EfficientNetV2-S** architecture to classify over 50 different cattle breeds with high precision.

---

## 🚀 Features
- **Deep Learning Core**: Powered by PyTorch and EfficientNetV2-S.
- **50+ Breeds**: Identifies a wide variety of Indian and international cattle breeds.
- **Fast Inference**: Get results in seconds.
- **Modern UI**: A premium, responsive glassmorphism design.
- **Confidence Scores**: Displays the AI's confidence level for each prediction.
- **Safety Check**: Low-confidence images (non-cattle) are filtered out automatically.

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **Machine Learning**: PyTorch, Torchvision
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (ES6+)
- **Model Architecture**: EfficientNetV2-S

---

## 📂 Project Structure
```text
Cattle Breed/
├── app.py              # Main Flask application
├── model/              # Model architecture and saved weights (.pth)
├── static/             # Frontend assets (CSS, JS, Images, Uploads)
├── templates/          # HTML templates
├── utils/              # Preprocessing scripts and class labels
├── requirements.txt    # Python dependencies
└── run.bat             # Quick launch script (Windows)
```

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- Python 3.8 or higher installed on your system.
- (Optional) A virtual environment is recommended.

### 2. Install Dependencies
Open your terminal/command prompt in the project directory and run:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the Flask server by running:
```bash
python app.py
```
Once the server starts, open your browser and navigate to:
`http://127.0.0.1:5000`

---

## 🐄 Supported Breeds
The model can identify 50+ breeds, including:
- **Indian Breeds**: Gir, Sahiwal, Ongole, Tharparkar, Kankrej, Hallikar, etc.
- **International Breeds**: Ayrshire, Red Sindhi, and more.
*(Full list available in `utils/labels.json`)*

---

## 📝 Usage Steps
1. **Launch** the application.
2. **Upload** a clear image of a cattle (side view preferred for best results).
3. **Wait** for the AI to analyze the features.
4. **View** the predicted breed and confidence percentage.

---

## 🛡️ License
This project is for educational and research purposes.
