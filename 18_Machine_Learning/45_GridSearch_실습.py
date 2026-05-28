from sklearn.svm import SVC, SVR
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris, load_breast_cancer, load_digits, load_wine, load_diabetes
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


def SVC_붓꽃():
    X, y = load_iris(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    스케일러 = StandardScaler()
    X_train = 스케일러.fit_transform(X_train)
    X_test  = 스케일러.transform(X_test)

    그리드파람 = {
        'C'     : [0.1, 1, 10, 100],
        'gamma' : [0.001, 0.01, 0.1, 1],
        'kernel': ['rbf', 'linear'],
    }

    모델 = GridSearchCV(SVC(), 그리드파람, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)
    모델.fit(X_train, y_train)

    print("최적 파라미터 :", 모델.best_params_)
    print("최적 CV 정확도:", 모델.best_score_)
    print("테스트 정확도 :", 모델.best_estimator_.score(X_test, y_test))

SVC_붓꽃()


def SVC_유방암():
    X, y = load_breast_cancer(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    스케일러 = StandardScaler()
    X_train = 스케일러.fit_transform(X_train)
    X_test  = 스케일러.transform(X_test)

    그리드파람 = {
        'C'     : [0.1, 1, 10, 100],
        'gamma' : [0.001, 0.01, 0.1, 1],
        'kernel': ['rbf', 'linear'],
    }

    모델 = GridSearchCV(SVC(), 그리드파람, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)
    모델.fit(X_train, y_train)

    print("최적 파라미터 :", 모델.best_params_)
    print("최적 CV 정확도:", 모델.best_score_)
    print("테스트 정확도 :", 모델.best_estimator_.score(X_test, y_test))

SVC_유방암()


def 랜덤포레스트_와인():
    X, y = load_wine(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    스케일러 = StandardScaler()
    X_train = 스케일러.fit_transform(X_train)
    X_test  = 스케일러.transform(X_test)

    그리드파람 = {
        'n_estimators': [10, 100, 200],
        'max_depth'   : [None, 3, 5, 10],
    }

    모델 = GridSearchCV(RandomForestClassifier(), 그리드파람, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)
    모델.fit(X_train, y_train)

    print("최적 파라미터 :", 모델.best_params_)
    print("최적 CV 정확도:", 모델.best_score_)
    print("테스트 정확도 :", 모델.best_estimator_.score(X_test, y_test))

랜덤포레스트_와인()


def KNN_손글씨():
    X, y = load_digits(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    스케일러 = StandardScaler()
    X_train = 스케일러.fit_transform(X_train)
    X_test  = 스케일러.transform(X_test)

    그리드파람 = {
        'n_neighbors': [3, 5, 7, 9],
        'weights'    : ['uniform', 'distance'],
    }

    모델 = GridSearchCV(KNeighborsClassifier(), 그리드파람, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)
    모델.fit(X_train, y_train)

    print("최적 파라미터 :", 모델.best_params_)
    print("최적 CV 정확도:", 모델.best_score_)
    print("테스트 정확도 :", 모델.best_estimator_.score(X_test, y_test))

KNN_손글씨()


def SVR_당뇨병():
    X, y = load_diabetes(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    스케일러_X = StandardScaler()
    스케일러_y = StandardScaler()
    X_train   = 스케일러_X.fit_transform(X_train)
    X_test    = 스케일러_X.transform(X_test)
    y_train_s = 스케일러_y.fit_transform(y_train.reshape(-1, 1)).ravel()

    그리드파람 = {
        'C'      : [0.1, 1, 10, 100],
        'epsilon': [0.01, 0.1, 0.5, 1],
        'kernel' : ['rbf', 'linear'],
    }

    모델 = GridSearchCV(SVR(), 그리드파람, cv=5, scoring='neg_mean_squared_error', n_jobs=-1, verbose=1)
    모델.fit(X_train, y_train_s)

    pred_s = 모델.best_estimator_.predict(X_test)
    pred   = 스케일러_y.inverse_transform(pred_s.reshape(-1, 1)).ravel()

    print("최적 파라미터 :", 모델.best_params_)
    print("MSE :", mean_squared_error(y_test, pred))

SVR_당뇨병()