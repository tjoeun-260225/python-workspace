import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 수집한 데이터 시각화여 확인
def 산점도확인():
    # 1. 산점도를 이용해서 꽃들이 어디 모여있는지 조회
    붓꽃 = load_iris()
    X = 붓꽃.data
    y = 붓꽃.target

    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    # 종류별로 다른 색을 지정하여 조회
    색깔 = ['red', 'blue', 'green']
    종류 = ['setosa', 'versicolor', 'virginica']
    plt.figure(figsize=(8, 5))  # 그래프가 들어있는 화면 전체 크기 설정

    # 데이터는 정말 다양하고, 많은 방식으로 존재
    # 아래 for문은 붓꽃에 해당하는 데이터 분포를 보기위한 용도중 하나일 뿐
    # 외우거나 익혀야할 필요 없다.
    for i in range(3): # setosa versicolor virginica 정답이 3개이므로 012 까지 조회  3은 자동으로 하지 않는 방식
        plt.scatter( # 산점도 분포를 할 때

        # X=데이터에서 y=정답이 0==0일때
            X[y == i, 0],  # x축 : 꽃받침 길이 X[y == i, 0] X 에서  y == i 같은것만 조회하여 0번열(꽃받침 길이만 갖고와)
            X[y == i, 1],  # y축 : 꽃받침 너비 y[y == i, 0] X 에서  y == i 같은것만 조회하여 1번열(꽃받침 너비만 갖고와)
            color=색깔[i],
            label=종류[i]
        )
    """
    i = 0 일 때 → setosa     데이터만 뽑아서 x축 꽃받침 길이, y축 꽃받침 너비로 빨간색 점으로 찍기
    i = 1 일 때 → versicolor 데이터만 뽑아서 x축 꽃받침 길이, y축 꽃받침 너비로 파란색 점으로 찍기
    i = 2 일 때 → virginica  데이터만 뽑아서 x축 꽃받침 길이, y축 꽃받침 너비로 초록색 점으로 찍기
    
    3종류를 각각 다른 색으로 점 찍어줘
    """
    plt.xlabel("꽃받침 길이")
    plt.ylabel("꽃받침 너비")
    plt.title("붓꽃 종류별 분포")
    plt.legend() # 어떤색이 어떤 종류인지 표기 화면에 보여주기
    plt.show() # 위에 작성한 것을 토대로 개발자의 눈에서 확인하기


# 막대그래프를 이용해서 종류별 개수 확인 가능

# 히트맵을 이용해서 어떤 특징이 중요한가 조회