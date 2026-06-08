from transformers import pipeline

# 1. 한국어 감정분석
def 한국어감정분석():
    분석모델 = pipeline(
        "sentiment-analysis",
        model = "monologg/koelectra-base-finetuned-sentiment",
        device=0, # GPU 사용 device=-1 CPU 사용
    )
    print(분석모델("이 영화 진짜 최고야!!!"))

한국어감정분석()