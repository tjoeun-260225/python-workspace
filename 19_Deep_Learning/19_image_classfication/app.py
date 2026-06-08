from flask import Flask, request, jsonify, render_template
from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image
import torch
import io

app = Flask(__name__)

print("모델 불러오는 중...")
processor = ViTImageProcessor.from_pretrained("./model")
model = ViTForImageClassification.from_pretrained("./model")
model.eval()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    image = Image.open(io.BytesIO(file.read())).convert("RGB")

    inputs = processor(images=image, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)[0]
    top3 = torch.topk(probs, 3)

    results = []
    for score, idx in zip(top3.values, top3.indices):
        label = model.config.id2label[idx.item()]
        results.append({
            "label": label,
            "score": round(score.item() * 100, 1)
        })

    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)