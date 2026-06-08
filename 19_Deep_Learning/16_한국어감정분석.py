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
classifier = pipeline(
    'sentiment-analysis',    # 나 이런작업을 할거야~ 허깅페이스에 알려주는 것
    model='snunlp/KR-FinBert-SC'  # 한국어 감정분석 모델 - 허깅페이스가 딥러닝으로 만듦
)
"""
허깅페이스에서 제공하는 ai로만 사용해도 어지간한 모델 하나 만들 수 있다.
-- 머신러닝, 딥러닝, 모두 좋으나 모델만드는게 목적이라면 허깅페이스만 잘 사용해도 된다.

허깅페이스
프랑스 개발자 = 클레망 델랑그, 줄리앙 쇼몽, 토마 울프 3명이 2016년에 만듦
처음에는 AI 회사가 아니었다.
2016년에 10대 청소년용 챗봇 앱을 만들고 친구처럼 대화하는 앱을 만들자! 잘 되지 않았음
챗봇 만들면서 쓴 AI길술을 오픈소스로 공개

개발자들에게 엄청난 인기

방향을 틀어서 AI 플랫폼 회사로 전환

기업 가치 5조원 2023년 기준 모델 90만개 이상 보유 구글 엔비디아 아마존 등 투자
AI 개발자들 사이에서 AI의 깃허브라고 불림

허깅페이스에서 제공하는 한국어 기반 감정 분석 추천 모델
snunlp/KR-FinBert-SC = 금융용 분석 데이터
monologg/koelectra-base~~~ = 영화/리뷰 감정 분석전용 positive negative
whitepeak~~                = 고객 리뷰 기반 학습     positive negative
tabularisai~~              = 한국어 포함 다국어 지원

이미지 관련된 모델들 다수 존재
google/ vie             이미지 분류
물체 감지
얼굴 감지

"""
# 테스트
리뷰들 = [
    "이 영화 진짜 최고야 완전 재미있어",
    "너무 지루하고 최악이었음 돈 아깝다",
    "배우 연기는 좋은데 스토리가 별로다"
]

for 리뷰 in 리뷰들:
    결과 = classifier(리뷰)[0]
    print(f"리뷰 : {리뷰}")
    print(f"결과 : {결과['label']} / 확신도 : {결과['score'] * 100:.1f}%")

"""
positive → 긍정
negative → 부정
neutral  → 중립 (애매한 것)
"""