'''
Pandas - 파이썬에서 표(테이블) 형태의 데이터를 다루는 라이브러리
엑셀과 비슷하다고 생각하면 된다.

pip install pandas

기본 사용법
import pandas as pd
* as = alias = 별명, 별칭
import pandas 작성해도 되지만... pandas 가 너~무 길어서 pd 라는 이름으로 줄여서 사용하겠다.

# 파일 불러오기 기본 인코딩 형식 encoding="utf-8" 기본값 으로 작성하지 않아도 된다.
pd.read_csv("파일이름.csv")

# 파일에 내용 작성하기
df = pd.DataFrame(dict(데이터 형식))
df.to_csv("만들파일이름.csv")
to_csv 와 같은 형식으로 만들 때에는 컬럼의 이름들과 각 컬럼에 들어갈 데이터를 설정 해주어야 한다.
'''
import pandas as pd
from pandas import pivot

# df = pd.read_csv("행정안전부_착한가격업소 현황_20260331.csv")
# 보통 한국에서 만든 csv 파일은 cp949 = 한국 버전 한국어 ←→ 컴퓨터 언어 상호작용 형태로 파일이 만들어진다.

# cp949 = EUC-KR 한국버전 컴퓨터 상호작용 표기법이다.
df = pd.read_csv("행정안전부_착한가격업소_현황_20260331.csv", encoding="cp949")


def 데이터기본정보조회():
    헤드 = df.head()  # 상위 5개의 행 갖고오기 -> 기본으로 출력이 없으므로 상위 5개의 행을 보고싶다면 print() 이용한다.
    print("상위 5개의 행 : ", 헤드)
    꼬리 = df.tail()
    print("아래 5개의 행 : ", 꼬리)
    print("=" * 60)  # = 60개 만들기 자바에서는 repeat() 기능 존재
    ### head() 와 tail() 소괄호 안에 숫자를 작성하지 않으면 기본으로 5개 1~n개 작성 가능

    헤드_10개 = df.head(10)  # 상위 5개의 행 갖고오기 -> 기본으로 출력이 없으므로 상위 5개의 행을 보고싶다면 print() 이용한다.
    print("상위 10개의 행 : ", 헤드_10개)
    꼬리_20개 = df.tail(20)
    print("아래 20개의 행 : ", 꼬리_20개)
    # 하위 5개의 행 갖고오기
    # -> 기본으로 데이터를 갖고오는 것이지 출력이 없으므로 print() 이용해서 어떤 데이터를 갖고왔는지 확인한다.
    print("=" * 60)
    행과열의개수 = df.shape
    print("행과 열의 개수 : ", 행과열의개수)
    print("=" * 60)
    csv_정보 = df.info()  # 데이터 타입, 결측치 확인
    print("csv 정보 : ", csv_정보)
    print("=" * 60)
    csv_요약정보 = df.describe()  # 평균, 최소, 최대 등 통계 요약
    print("csv 요약정보 : ", csv_요약정보)


'''
데이터 정제      
다수 컬럼에서 필요한 열만 뽑거나 특정조건에 맞는 행만 남기는 행위

열 선택하기
모든 정보가 다 필요하지 않을 때 원하는 컬럼만 리스트 형식으로 가져온다.
'''


# df = pd.read_csv("행정안전부_착한가격업소 현황_20260331.csv", encoding="cp949")
def 데이터정제조회():
    df_컬럼들 = df[['업소명', '시도', "메뉴1", "가격1"]]
    df_컬럼 = df['업소명']
    print(df_컬럼들.head())
    print(df_컬럼.head())
    시도명_서울 = df[df['시도'] == '서울특별시']
    print("서울 소재 업소 수 : ", len(시도명_서울))


'''
결측치 = 데이터가 없는 것
0 + ""  = 컴퓨터 에러 발생 0이랑 빈값이랑 어떻게 더하라고
1 + NaN = 뭐하라는 거지..? 난 할 수 없어 컴퓨터 에러 발생

NaN = 값이 없음(빈칸) 이라는 표시 기법
'''


def 데이터결측치_정리_조회():
    # df = csv 파일에서  isnull() 빈칸인게 있나요?  .sum 총 몇 개죠?
    데이터가_없는_개수확인 = df.isnull().sum()
    print("데이터가 없는 개수확인 : ", 데이터가_없는_개수확인)

    # drop 삭제할게~ na NaN 값을    NaN 빈값으로 되어 있는 칸 삭제
    데이터가_없는_행삭제 = df.dropna()
    print("데이터가 없는 행삭제 : ", 데이터가_없는_행삭제)

    # fill 채우다   na NaN 값을    0으로 채워넣겠다. 계산하기 편하게
    데이터가_없는_행_0으로_채우기 = df.fillna(0)
    print("데이터가 없는 행 0으로 채우기 : ", 데이터가_없는_행_0으로_채우기)
    데이터가_없는_행_없음으로_채우기 = df.fillna("없음")
    print("데이터가 없는 행 없음으로 채우기 : ", 데이터가_없는_행_없음으로_채우기)
    # 데이터가_없는_행_평균값_으로_채우기 = df.fillna(df.mean())
    # 숫자 컬럼만 골라서 평균 채우기 문자열은 하지마
    데이터가_없는_행_평균값_으로_채우기 = df.fillna(df.mean(numeric_only=True))
    print("데이터가 없는 행 평균값으로 채우기 : ", 데이터가_없는_행_평균값_으로_채우기)


# 데이터결측치_정리_조회()
# 데이터정제조회()


def 배열_1차원배열_2차원배열():
    # Series 1차원 배열
    s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    # DataFrame 2차원 배열
    # dict은 {} 축약형으로
    # df_dict과 df_중괄호 는 같은 결과 같은의미 같은 뜻으로 작성 방식만 다르다.
    df_dict = pd.DataFrame(
        dict(
            name=['Alice', "Bob", "Charlie"],
            age=[25, 30, 35],
            score=[90, 85, 92]
        )
    )
    df_중괄호 = pd.DataFrame(
        {
            'name': ['Alice', "Bob", "Charlie"],
            'age': [25, 30, 35],
            'score': [90, 85, 92]
        }
    )
    # 대부분의 데이터 구조는 다차원 구조


def 머지_콘캣_피벗테이블():
    df1 = pd.DataFrame(
        dict(
            id=[1, 2, 3],
            name=['A', 'B', 'C']
        )
    )
    df2 = pd.DataFrame(
        dict(
            id=[1, 2, 3],
            score=[90, 85, 92]
        )
    )
    # 개별로 존재하는 테이블 합치기
    # SELECT  s.가게이름, o.주문번호
    # FROM 가게 s, 주문 o
    # WHERE s.id = o.id
    #   판다스에서 합치기 기능을 가져와 사용하겠다.      1번 데이터틀과 2번 데이터틀을 합칠 것인데,
    #                                            on=합치는 기준(= 두 컬럼에 동일하게 존재하는 컬럼이름 작성)
    #   pd    .             merge                     (df1, df2, on='id')
    # 머지는 두 DataFrame만 합치기 가능
    합치기 = pd.merge(df1, df2, on='id')  # SQL JOIN 문처럼 합칠 기준이 되는 컬럼 설정
    print(합치기)
    '''
       id name  score
    0   1    A     90
    1   2    B     85
    2   3    C     92
    '''

    # concat = 위 아래 또는 옆으로 붙이기
    df_a = pd.DataFrame(
        dict(
            name=['A', 'B']
        )
    )
    df_b = pd.DataFrame(
        dict(
            name=['C', 'D']
        )
    )

    # 판다스에서       합칠 DataFrame 을 [] 넣기 개수 제한 없음   붙이기전 원본 인덱스를 무시하고 0부터 새롭게 번호매김 시작하겠다.
    # pd       .    concat(             [df_a,           df_b], ignore_index=True)
    result1 = pd.concat([df_a, df_b], ignore_index=True)
    result2 = pd.concat([df_a, df_b])  # ignore_index=False 가 기본값 데이터 그대로 유지하면서 합치도록해~
    print(result2)
    '''
    ####result1
           name
        0    A
        1    B
        2    C
        3    D
    ####result2 기존 각 컬럼에 존재하는 번호판을 그대로 유지하면서 데이터 추가
          name
        0    A
        1    B
        0    C
        1    D

    '''


def 필터링_정렬_그룹화():
    # 필터링 : 조건으로 행 추려내기

    # 나이 30이상만 목록에서 조회하기
    df[df['컬럼이름'] >= 30]  # 특정 컬럼에서 29 이하인 데이터는 모두 안녕~

    # 여러 조건 ( & | 사용)

    # df[(       조건1번      ) 둘 중 하나 True 일 경우 OK True다 (        조건2번      )]
    # df[(df['컬럼이름'] >= 25)                |                 (df['컬럼이름'] >= 85)]
    # df[(       조건1번      ) 모두 True 일 경우에만 (        조건2번      )]
    # df[(df['컬럼이름'] >= 25)       &               (df['컬럼이름'] >= 85)]
    df[(df['컬럼이름'] >= 25) & (df['컬럼이름'] >= 85)]

    # 정렬 : sort_values
    df.sort_values('컬럼이름', ascending=False)  # 컬럼데이터 내림차순
    df.sort_values('컬럼이름')  # 컬럼데이터 오름차순 기본값
    df.sort_values(['컬럼이름1번', '컬럼이름2번'], ascending=[True, False])  # 컬럼1번은 오름차순 컬럼2번은 내림차순
    # 다중정렬

    # 그룹화
    df.groupby('name')['score'].mean()  # 이름컬럼에서 동일한 이름들의 평균 점수
    df.groupby('name')['score'].agg(  # 여러 집계
        {'score': 'mean',
         'age': 'max'}
    )


def 피벗테이블():
    # 피벗(pivot) : 중심축, 회전축
    # 프랑스에서 넘어온 단어, 물리적으로 무언가가 그 위에서 회전하는 고정된 핀이나 축
    # 농구에서 피벗 - 한 발을 고정하고 몸을 돌리는 동작
    # 스타트업에서 피벗선언!!! - 핵심은 유지하면서 사업방향을 전환
    # 데이터에서 피벗이란
    # 데이터를 축 중심으로 회전시켜 보는 각도를 다르게 하겠다

    df.pivot_table(
        values='score',  # 숫자로 채울 데이터
        index='name',  # 행 기준 (세로)
        columns='subject'  # 열 기준 (가로)
        , aggfunc='mean'  # 집계 방법 (평균, 합계 등)
    )
    # index = 왼쪽에 세울 것 columns = 위에 펼칠 것 values = 안에 채울 데이터


def 피벗테이블예시():
    df = pd.DataFrame(
        dict(
            name=['Alice', 'Alice', 'Bob', 'Bob'],
            subject=['math', 'english', 'math', 'english'],
            score=[90, 85, 80, 75]
        )
    )
    print("========== 피벗 전 데이터 확인 ==========")
    print(df)
    피벗작업 = df.pivot_table(
        values='score',
        index='name',
        columns='subject',
        aggfunc='mean'
    )
    print("========== 피벗 후 데이터 확인 ==========")
    print(피벗작업)

# 머지_콘캣_피벗테이블()
피벗테이블예시()
'''
========== 피벗 전 데이터 확인 ==========
    name  subject  score
0  Alice     math     90
1  Alice  english     85
2    Bob     math     80
3    Bob  english     75

피전 전은 4행 짜리 긴 데이터였다.
피벗 후엔 name 기준 2행으로 줄고,
subject 가 열로 펼쳐진 상태
.0 붙은 것은     aggfunc='mean'    때문에 float 형태로 변환

평균 = 기본 세팅 float 실수
========== 피벗 후 데이터 확인 ==========
subject  english  math
name                  
Alice       85.0  90.0
Bob         75.0  80.0

'''