import os

"""
한국어 감정 분석
1. KoBERT
- 카카오브레인이 만든 한국어 특화 BERT 모델
- AI를 공부하는 설치도 까다롭고, 무겁다
- 대신 같은 원리이지만 더 쉬운 라이브러리가 존재
* BERT : 구글이 만든 Transformer 기반 언어 모델 그걸 한국어로 학습시킨 것

IMDB 모델이 영어만 공부한 뇌 라면
KoBERT 는 한국어만 공부한 뇌

2. HuggingFace (허깅페이스)
- 한국어 감정 분석 모델 제공
- pip install transformers torch

torch 와 tensorflow 는 하는 일은 같지만 딥러닝 프레임워크를 만든 회사가 다르다.
               Tensorflow         PyTorch
만든곳            구글          페이스북(Meta)
별  명             TF               torch
특  징     배포/서비스강함    연구/실험에 강함
사  용         국내 실무      논문 / AI 연구자

삼성 / 아이폰처럼 하는 일은 같지만 회사가 다르다.
구글이 제공하는 기능들을 페이스북이 더 성능좋고, 가볍게 기능들을 대부분 제공

AI는 파이토치 가 대세
Microsoft → Google → FaceBook
"""
from transformers import pipeline

# import torch

# 한국어 감정분석 모델 불러오기(자동 다운로드)
classfier = pipeline(
    'sentiment-analysis',
    model='snunlp/KR-FinBert-SC'  # 한국어 감정분석 모델 - 허깅페이스가 딥러닝으로 만듦
)

# 테스트
리뷰들 = [
    "이 영화 진짜 최고야 완전 재미있어",
    "너무 지루하고 최악이었음 돈 아깝다",
    "배우 연기는 좋은데 스토리가 별로다"
]

for 리뷰 in 리뷰들:
    결과 = classfier(리뷰)[0]
    print(f"리뷰 : {리뷰}")
    print(f"결과 : {결과['label']} / 확신도 : {결과['score'] * 100:/1f}%")
