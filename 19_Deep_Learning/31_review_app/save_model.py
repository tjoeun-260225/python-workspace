"""
실행: python save_model.py
결과: saved_model/ 폴더 생성
"""

import os, json, torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
# 나의 컴퓨터로 허깅페이스에 저장되어 있는
# 남이 만든 ai 모델 다운로드해서 사용
# 최초 1회 다운로드
MODEL_NAME_1 = "nlptown/bert-base-multilingual-uncased-sentiment"
MODEL_NAME_2 = "hun3359/klue-bert-base-sentiment"
SAVE_DIR   = "saved_model"
MAX_LEN    = 128

# ── 1. 모델 + 토크나이저 다운로드 ──────────────────────
print("모델 다운로드 중... (최초 1회 약 700MB)")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME_2)
pt_model  = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME_2)
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
# 한국어 동작은 하지만 정식 지원이 아니라서
# 한국어 에서는 애매한 문장에 오류 발생
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
    "model_name" : MODEL_NAME_2,
    "max_len"    : MAX_LEN,
    "format"     : "keras_wrapper",
    "id2label"   : pt_model.config.id2label,          # {"0":"1 star", ...}
}
with open(f"{SAVE_DIR}/model_meta.json", "w", encoding="utf-8") as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)

print(f"\n저장 완료 → ./{SAVE_DIR}/")
print("다음 단계: python app.py")