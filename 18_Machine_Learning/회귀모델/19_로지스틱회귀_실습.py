from sklearn.datasets import load_iris, load_wine, load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 우리가 기존에 공부했던 실습 코드 방향을 100% 인지한 상황부터 사용
def 로지스틱모델기능(데이터, name, max_iter=1000):
    X, y = 데이터.data, 데이터.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=max_iter)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"{name} 정확도 :{score:.2f}")
    return model # 지금은 의미가 없지만 나중에 만들어놓은 모델을 재사용해야할 때 사용할 수 있다.

#  함수를 호출해서 사용하기
# 정확도에 대한 결과만 확인할 때 작성
로지스틱모델기능(load_iris(),"붓꽃")
로지스틱모델기능(load_wine(),"와인")
로지스틱모델기능(load_digits(),"손글씨", max_iter=5000) # 기본값 1000 대신 5000 사용

model_iris = 로지스틱모델기능(load_iris(),"붓꽃")
model_wine = 로지스틱모델기능(load_wine(),"와인")
model_digits = 로지스틱모델기능(load_digits(),"손글씨", max_iter=5000)
# 각각 만들어진 모델로 무언가 작업을 하거나 시각화 처리를 하는 등 다양한 방식에서 활용하려면
# 위와 같이 변수공간에 model 결과를 담아 사용




# 반복적인 작업을 함수화하여 반복 줄이기
# data1 = load_iris()
# data2 = load_wine()
# data3 = load_digits()
#
# X1, y1 = data1.data, data1.target
# X2, y2 = data2.data, data2.target
# X3, y3 = data3.data, data3.target
#
# X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
# X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
# X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)
#
# model = LogisticRegression(max_iter=200)
# model.fit(X1_train, y1_train)
# print("정확도 :", model.score(X1_test, y1_test))
