"""
실행: python app.py
접속: http://127.0.0.1:5000
"""

import json, torch
from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

SAVE_DIR = "saved_model"
MAX_LEN  = 128

# ── 모델 로드 (서버 시작 시 1회) ───────────────────────
print("저장된 모델 불러오는 중...")

with open(f"{SAVE_DIR}/model_meta.json", encoding="utf-8") as f:
    meta = json.load(f)

tokenizer = AutoTokenizer.from_pretrained(f"{SAVE_DIR}/tokenizer")
model     = AutoModelForSequenceClassification.from_pretrained(f"{SAVE_DIR}/pt_weights")
model.eval()

print("모델 로드 완료")

# ── 예측 함수 ──────────────────────────────────────────
def predict_stars(text: str) -> dict:
    """
    텍스트 → 별점 예측
    반환: {stars, score, all_probs}
    """
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=MAX_LEN,
        truncation=True,
        padding="max_length",
    )
    with torch.no_grad():
        logits = model(**inputs).logits             # shape: (1, 5)

    probs     = torch.softmax(logits, dim=-1)[0]    # 5개 확률값
    pred_idx  = torch.argmax(probs).item()          # 최고 확률 인덱스 (0~4)
    label     = model.config.id2label[pred_idx]     # "3 stars"
    stars     = int(label.split()[0])               # 3

    return {
        "stars"     : stars,
        "score"     : round(probs[pred_idx].item(), 4),
        "all_probs" : [round(p.item(), 4) for p in probs],  # [1★, 2★, 3★, 4★, 5★]
    }

# ── 라우트 ─────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "텍스트를 입력해주세요."}), 400
    if len(text) > 512:
        return jsonify({"error": "512자 이하로 입력해주세요."}), 400

    result = predict_stars(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)