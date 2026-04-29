# aka pandas 회사 것을 가져왔지만 너~무 길어서 pd로 쓸게 ^^
# docs 작성되어 있고,,
# 결측치 = 없을 결 측정할 측 값 치    측정할게 없는 값 빈 값  데이터가 비어있는 칸
import pandas as pd

# 1. 불러오기 (한글 파일은 cp949 인코딩)
df = pd.read_csv("행정안전부_착한가격업소 현황_20260331.csv", encoding="cp949")

# 2. 기본 확인
print(df.shape) # 행 수 열 수
print(df.columns) # 컬럼이름 목록
print(df.head()) # 상위 5개의 행
print(df.tail()) # 하위 5개의 행
print(df.info())  # 컬럼별 타입 + 결측치 수
# 결측치(나중에 데이터가 없는 칸)은 0으로 만들거나 하여 계산을 할 때 문제없도록 처리해야함
# 0 + "" = 숫자끼리만 더할 수 있어요 에러 발생  NaN = 데이터 없어요~
print(df.describe()) # 수치형 컬럼 통계 요약