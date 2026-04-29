# 스켈레톤 코드 = 뼈대 코드
from playwright.sync_api import sync_playwright
import time
import csv
import pandas as pd

'''
playwright 시작
    → 브라우저 열기
        → 검색어마다 페이지 이동
            → 제목 + 본문 가져오기
                → 결과 리스트에 추가
    → 브라우저 닫기
→ playwright 종료
→ CSV 파일로 저장
'''


def 나무위키_기본CSV버전():
    # TODO___ playwright 실행 시작
    p = ___

    # TODO___ 크롬 브라우저 열기 (창 보이게)
    browser = ___

    # TODO___ 새 탭 열기
    page = ___

    검색어목록 = ["강아지", "고양이", "토끼"]

    # TODO___ 결과를 담을 빈 리스트 만들기
    결과리스트 = ___

    for 검색 in 검색어목록:
        # TODO___ 나무위키 해당 검색어 페이지로 이동
        page.goto(___)
        time.sleep(2)

        # TODO___ 브라우저 탭 제목 가져오기
        제목 = ___

        # TODO___ body 태그 안의 텍스트 가져오기
        본문 = ___

        print(f"=== {검색}")
        print(f"제목 : {제목}")
        print(f"본문 앞부분 : {본문[:300]}")
        print()

        # TODO___ 검색어, 제목, 본문앞300자 를 결과리스트에 추가
        결과리스트.append(___)
        time.sleep(2)

    browser.close()
    p.stop()

    # TODO___ csv 파일 열기 (파일명: 나무위키결과.csv, 한글깨짐 방지)
    f = open(___)

    # TODO___ csv writer 만들기
    writer = ___

    # TODO___ 컬럼 이름 쓰기 (검색어, 제목, 본문)
    writer.writerow(___)

    # TODO___ 결과리스트 전체 저장
    writer.writerows(___)

    # TODO___ 파일 닫기
    ___

    print("기본CSV 저장 완료!")


def 나무위키_pandasCSV버전():
    # TODO___ playwright 실행 시작
    p = ___

    # TODO___ 크롬 브라우저 열기 (창 보이게)
    browser = ___

    # TODO___ 새 탭 열기
    page = ___

    검색어목록 = ["강아지", "고양이", "토끼"]

    # TODO___ 결과를 담을 빈 리스트 만들기
    결과리스트 = ___

    for 검색 in 검색어목록:
        # TODO___ 나무위키 해당 검색어 페이지로 이동
        page.goto(___)
        time.sleep(2)

        # TODO___ 브라우저 탭 제목 가져오기
        제목 = ___

        # TODO___ body 태그 안의 텍스트 가져오기
        본문 = ___

        print(f"=== {검색}")
        print(f"제목 : {제목}")
        print(f"본문 앞부분 : {본문[:300]}")
        print()

        # TODO___ 검색어, 제목, 본문앞300자 를 결과리스트에 추가
        결과리스트.append(___)
        time.sleep(2)

    browser.close()
    p.stop()

    # TODO___ 결과리스트로 DataFrame 만들기 (컬럼: 검색어, 제목, 본문)
    df = pd.DataFrame(___)

    # TODO___ CSV로 저장 (파일명: 나무위키결과.csv, index 없이, 한글깨짐 방지)
    df.to_csv(___)

    print("pandas CSV 저장 완료!")


# TODO___ 두 함수 중 하나 실행해보기
나무위키_기본CSV버전()
# 나무위키_pandasCSV버전()