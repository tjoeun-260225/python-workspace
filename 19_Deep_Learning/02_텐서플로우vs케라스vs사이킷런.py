import os

"""
scikit-learn
- 머신러닝 라이브러리
- 선형 회귀, 결정 트리, 랜덤포레스트 등 전통적인 알고리즘이 존재
- GPU를 사용하지 않으며, 데이터 전처리, 모델 평가, 교차검증 도구에 있어
  딥러닝 프로젝트에서도 전처리 단계에서 자주 사용된다.
  데이터 작업 처리 사용
TensorFlow
- 구글이 만든 딥러닝 프레임워크
- TensorFlow 는 행렬 미분, 역전파, GPU 메모리 관리를 모두 작성해야하는 번거로움 해소
  초기에 개발을 배울 때 사용 실무에서는 사용을 거의 안한다.
Keras
- TensorFlow 위에서 동작하는 고수준 API
- 레이어 쌓고, 컴파일하고, 학습시키는 것을 몇 줄로 끝낸다.
- 초기에 개발을 배울 때 사용 실무에서는 사용을 거의 안한다.

위 세가지는 가끔 사용하기는 하나 우리가 처음에 스스로 밥을 먹기 전까지
어른들, 도구의 도움을 받지만 (=scikit-learn, TensorFlow, Keras) 
나중에 스스로 먹을 수 있는 것처럼 나중에 개발자들은 컴퓨터에 대한 자아가 생성되고,
목표와 자아에 따라 직접적으로 모든 것을 세팅하길 원한다.

회사에서 지정하는 목표, 선호는 모델에 따라 어떤 전처리, 어떤 모델, 어떤 학습을 시키게 될지는
알 수 없다.

하지만 

데이터 수집 - 전처리 - 모델 - 학습 - 학습할 때 커스텀을 해주면 정확도가 올라갈 수 있다.

와 같은 개념을 이해하고 공부하기 위하여 필요

딥러닝에서 초기에 텐서플로우와 케라스 설치 필요

구글에서 인정하는 텐서플로우 자격증은 그렇게까지 따는 추세는 지났다.
AICE - 국가에서 인정되는 단계 자격증 취득하는 것이 낫다.

텐서플로우와 케라스 설치 방법
pip install tensorflow 해주면 설치된다. 텐서플로우 안에 케라스가 내장되어 있다.
"""

# 1. 텐서플로우 케라스 환경 설치 & GPU 확인
# GTX1660은 CUDA 지원 GPU
# pip install tensorflow
import tensorflow as tf

# 설치된 텐서플로우 버전 확인
print(tf.__version__)

# GPU 인식 확인
gpus = tf.config.list_physical_devices("GPU")
print("인식된 GPU : ", gpus)

# CUDA, cuDNN 버전 확인
print("CUDA : ",tf.sysconfig.get_build_info()['cuda_version'])
print("cuDNN : ",tf.sysconfig.get_build_info()['cudnn_version'])

'''
# TensorFlow 2.11 버전부터 windows 환경에서는 GPU를공식 지원하지 않는다.
# 구글이 정책을 바꿨으며, CUDA를 설치했어도 GPU 인식이 안된다.
# 텐서플로우 2.21 이기 때문이다.
WARNING:tensorflow:TensorFlow GPU support is not available on native Windows for 
TensorFlow >= 2.11. Even if CUDA/cuDNN are installed, GPU will not be used. 
Please use WSL2 or the TensorFlow-DirectML plugin.
Traceback (most recent call last):

print("CUDA : ",tf.sysconfig.get_build_info()['cuda_version'])
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
KeyError: 'cuda_version'
2.21.0
인식된 GPU :  []  # GPU가 고장난게 아니고 TensorFlow가 window에서 GPU를 의도적으로 안쓰는 것


1번 다운그레이드
pip uninstall tensorflow 삭제
pip install   tensorflow==2.10.0 
으로 다운그레이드

2번 tensorflow-directml 플러인 설치
에러 메세지에서 나와있다.

Please use WSL2 or the TensorFlow-DirectML plugin.

Microsoft 가 만든 WindowsGPU 지원 플러그인이다.
pip install tensorflow-cpu
pip install tensorflow-directml-plugin
설치필요

딥러닝을 개발하는 개발자들이 윈도우 컴퓨터가 아니라 ubuntu나 맥북과 같은 컴퓨터
aws 와 같은 클라우드에서 딥러닝개발하는 것을 구글에서 확인

구글 입장에서는 window gpu 지원을 유지하는게 유지보수 비용 대비 사용자 적다.
구글자체에서 클라우드 판매
- 본인들이 판매하는 클라우드에서 gpu를 돌려라.
'''



"""
CPU 
- 1970년대 인텔이 최초의 상업용 CPU를 만들었다.
- 당시 컴퓨터가 만들어진 목적은 계산
  급여 계산, 회계 장부, 미사일 탄도 계산과 같은 반복적인 작업의 특징을 파악하여 기계로 작업하겠다.
  CPU 컴퓨터 설계 철학 : 하나의 복잡한 일을 빠르게
            워드 켜고, 파일 저장하고, 인터넷 연결하는 작업들은 전부 순서가 있고 복잡
            CPU는 이러한 일들을 잘하기 위하여 생성된 부품  
  
GPU
- 1990년대 들어서 PC게임 시장이 커졌다.
- 게임 화면을 그리려면 모니터의 픽셀을 전부 계산
  예를 들어 모니터 사이즈 1920 X 1080 사이즈면 하나의 화면을 그리기 위해서 필요한 픽셀
  207만개 정도가 필요 초당 60프레임 1초에 1억 2천만 개의 픽셀 색상을 계산해야한다.
  
  픽셀 계산의 특징이 있다. 각 픽셀은 서로 독립적이다.
  CPU 로 계산을 하게 되면 순차작업으로 하나씩 계산하게 되어 너무 느리다.
  
  NVIDIA 1999년에 GPU 처음 생성
  코어 하나하나는 약하지만 수천 개를 동시에 작업할 수 있는 구조
  CPU는 순차작업을 하는 부품, GPU는 동시에 작업할 수 있는 부품
  게임 그래픽, 영상 디코딩/인코딩 게임 시뮬레이션에서 사용
  그러다 AI 연구자들이 GPU를 사용하면 모델을 빠르게 만들 수 있겠다! 생각하여
  CPU대신 GPU를 사용하게 되었다.
  2007년 부터 AI가 GPU를 사용함에 따라 NVIDIA 시가 총액이 좋아지는 상황 탄생!

  GPU는 원래화면에 픽셀을 그리는 용도로 만들어진 칩 = 이미지 용
    이미지에 특화
  GPU에서 프로그래밍을 위한 GPU를 만들어야겠다! AI에서 쓰네? 돈되겠네!
  2007년 CUDA - 파이썬과 같은 일반 이미지가 아닌 프로그래밍에서 사용할 수 있는
  드라이버 생성 Tensorflow 나 Pytorch 가 GPU 에 연산을 보낼 때 직접 GPU 칩에
  명령하는 게 아니라 CUDA를 통해서 나 프로그래밍코야~ 하고 GPU사용 하게 되는 것
  
  cuDNN
  - CUDA = 나 ~ 프로그래밍에서 GPU 쓸거야 통신 담당
  - cuDNN = 딥러닝 연산만 따로 뽑아서 극한까지 최적화한 라이브러리
    Nvidia 가 직접 딥러닝 연산에 GPU 성능을 더 좋게 사용할 수 있도록 튜닝해놓은 드라이버
    
  - cuDNN 없이 CUDA 만으로 딥러닝을 할 수 있지만 속도 차이가 난다.
    그래서 딥러닝 환경 세팅을 할 때 CUDA와 cuDNN을 함께 사용하여 속도를 향상 시키려 한다.
    
  GTX 1660이 CUDA 지원 GPU라는 의미
  - 엔비디아가 CUDA 라는 모델을 지원할 수 있는 부품을 더 비싸게 판다.
  - cuda 가 들어있는 컴퓨터는 구매할 수 없다 -> 와 같은 소비자를 위해
    gpu가 안되는 컴퓨터도 존재한다는 것
    
맥북 프로 - 영상 작업 가능
맥북 에어 - 영상 작업 하는 데 있어 사양 약하다.
GTX =맥북 이나 갤럭시처럼 부품의 모델 이름일 뿐이다.
s26 부터 전화할 때 상대방에게 용건을 물어보고 전화받을지 말지 결정 기능
s24는 주변사람지우기나 용건물어보고 받지말지 결정 기능 없다.
와 같은 상황이랑 유사하다.

GTX모델번호가 낮으면 GPU없다.
"""











