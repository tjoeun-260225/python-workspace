# 문제 1 - range 이용해서 1~100 합계 구하기
def 합계구하기():
    total = 0
    for i in range(1,101):
        total += i
    #    print(f"1부터 100까지 합계: {total}") 1부터 모든 결과 조회
    print(f"1부터 100까지 합계: {total}") # 맨 마지막 결과만 조회

합계구하기()
# 결과: 1부터 100까지 합계: 5050
