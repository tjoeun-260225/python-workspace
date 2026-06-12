import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split

이미지크기 = 64


def 이미지불러오기(폴더경로):
    이미지목록 = []
    for 파일명 in os.listdir(폴더경로):
        if not 파일명.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        try:
            경로 = os.path.join(폴더경로, 파일명)
            img = Image.open(경로)
            img = img.convert("RGB")
            img = img.resize((이미지크기, 이미지크기))
            이미지목록.append(np.array(img))
        except Exception as e:
            print(f"실패: {파일명} - {e}")
    print(f"불러온 이미지 수: {len(이미지목록)}")
    return np.array(이미지목록)


def 데이터준비():
    토끼데이터 = 이미지불러오기("rabbit")
    토끼데이터 = 토끼데이터.astype("float32") / 255.0
    토끼_펼친것 = 토끼데이터.reshape(-1, 이미지크기 * 이미지크기 * 3)
    print(f"최종 데이터 형태: {토끼_펼친것.shape}")
    훈련, 테스트 = train_test_split(토끼_펼친것, test_size=0.2, random_state=42)
    print(f"훈련: {훈련.shape}, 테스트: {테스트.shape}")
    return 훈련, 테스트
