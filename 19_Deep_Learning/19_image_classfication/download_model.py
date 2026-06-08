# 인터넷에서 허깅페이스 개발자가 만든 모델을
# 나의 컴퓨터에 저장한다.
from transformers import ViTForImageClassification, ViTImageProcessor

model_name = "google/vit-base-patch16-224"
save_path = "./model"

print("모델 다운로드 중...")
processor = ViTImageProcessor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

processor.save_pretrained(save_path)
model.save_pretrained(save_path)

print("저장 완료 ./model 폴더에 저장됐습니다.")