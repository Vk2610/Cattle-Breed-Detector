import os
import json
import torch
import torch.nn.functional as F
from PIL import Image
from flask import Flask, render_template, request, jsonify

from model.model import CattleModel
from utils.preprocess import transform

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# -------------------------------------------------------------
# 1. Model Loading
# -------------------------------------------------------------
def load_model():
    with open("utils/labels.json") as f:
        labels = json.load(f)
    model = CattleModel(num_classes=len(labels))
    model.load_state_dict(torch.load("model/model.pth", map_location=torch.device('cpu')))
    model.eval()
    return labels, model

labels, model = load_model()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("image")
        if file:
            # Save image
            filename = file.filename
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_path)

            # AI Inference
            image = Image.open(image_path).convert('RGB')
            img_tensor = transform(image).unsqueeze(0)
            
            with torch.no_grad():
                output = model(img_tensor)
                probabilities = F.softmax(output[0], dim=0)
                top_probs, top_indices = torch.topk(probabilities, 5)
            
            primary_breed = labels[top_indices[0].item()].title().replace("_", " ")
            primary_conf = top_probs[0].item() * 100

            # Low confidence check
            if primary_conf < 65.0:
                return jsonify({
                    "error": "No cattle detected",
                    "message": "Please upload a clear cattle image."
                })

            # Get Top 3 for the UI
            top3 = []
            for i in range(3):
                idx = top_indices[i].item()
                prob = top_probs[i].item()
                top3.append({
                    "breed": labels[idx].title().replace("_", " "),
                    "confidence": round(prob * 100, 1)
                })

            return jsonify({
                "prediction": primary_breed,
                "confidence": round(primary_conf, 1),
                "top3": top3,
                "image_path": image_path
            })

    return render_template("index.html")

    return render_template("index.html")

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
