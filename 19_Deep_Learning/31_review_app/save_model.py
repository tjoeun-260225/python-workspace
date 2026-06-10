"""
실행: python save_model.py
결과: saved_model/ 폴더 생성
"""

import os, json, torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"
SAVE_DIR   = "saved_model"
MAX_LEN    = 128

# ── 1. 모델 + 토크나이저 다운로드 ──────────────────────
print("모델 다운로드 중... (최초 1회 약 700MB)")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
pt_model  = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
pt_model.eval()

# ── 2. 동작 테스트 ─────────────────────────────────────
def quick_predict(text):
    inputs = tokenizer(text, return_tensors="pt",
                       max_length=MAX_LEN, truncation=True, padding="max_length")
    with torch.no_grad():
        logits = pt_model(**inputs).logits
    probs    = torch.softmax(logits, dim=-1)[0]
    pred_idx = torch.argmax(probs).item()
    label    = pt_model.config.id2label[pred_idx]   # ex) "3 stars"
    stars    = int(label.split()[0])                 # ex) 3
    return stars, round(probs[pred_idx].item(), 4)

test_texts = [
    "This product is absolutely amazing!",
    "정말 별로예요. 품질도 나쁘고 배송도 늦었어요.",
    "그냥 평범해요. 나쁘지도 좋지도 않아요.",
]
print("\n저장 전 테스트:")
for t in test_texts:
    stars, score = quick_predict(t)
    print(f"  {'⭐'*stars} ({stars}점, {score:.1%})  {t[:35]}")

# ── 3. 저장 ───────────────────────────────────────────
os.makedirs(SAVE_DIR, exist_ok=True)

tokenizer.save_pretrained(f"{SAVE_DIR}/tokenizer")    # 토크나이저
pt_model.save_pretrained(f"{SAVE_DIR}/pt_weights")    # 모델 가중치

# Keras 메타 파일 (.keras 역할 — 설정값 보존용)
meta = {
    "model_name" : MODEL_NAME,
    "max_len"    : MAX_LEN,
    "format"     : "keras_wrapper",
    "id2label"   : pt_model.config.id2label,          # {"0":"1 star", ...}
}
with open(f"{SAVE_DIR}/model_meta.json", "w", encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)

print(f"\n저장 완료 → ./{SAVE_DIR}/")
print("다음 단계: python app.py")