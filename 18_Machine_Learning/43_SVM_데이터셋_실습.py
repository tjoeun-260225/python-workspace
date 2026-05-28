from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # SVM은 스케일링 필수다.
def 붓꽃실습():
    X, y = load_iris(return_X_y=True)
    # csv 파일을 가져오지 않고 제공하는 데이터셋을 사용할 때 위와같이 작성한다.
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    clf = SVC(kernel='rbf', C=1.0, gamma='scale')
    clf.fit(X_train, y_train)

    print("SVC 정확도 : ", clf.score(X_test, y_test))
    print("예측값 :", clf.predict(X_test[:5]))
    print("실제값 : ", y_test[:5])

    """
    SVC 정확도 :  1.0 
    # 문제가 있는 것 붓꽃의 경우 너무 완벽하게 정제된 데이터라
    # 1.0 이 정상
    # 붓꽃과 같이 정제된 데이터가 아니면 비정상
    예측값 : [1 0 2 1 1]   ← 모델이 예측한 꽃 종류
    실제값 :  [1 0 2 1 1]  ← 실제로 정답인 꽃 종류
    모델이 예측한 답이랑 실제 정답을 나란히 놓고 비교한 상황
    숫자는 꽃 종류 번호
    """