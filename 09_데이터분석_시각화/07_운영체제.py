'''
os(Operating System)
- 운영체제와 상호작용하는 파이썬 기본 내장 모듈
파일 / 폴더 관련 작업을 코드로 할 수 있게 해줌
pip install 없이 바로 사용 가능
'''
import os

def 폴더작업():
    # 폴더 생성
    os.makedirs("새폴더") # 폴더만들기 동일한 명칭의 폴더가 이미 존재하면 에러 발생
    os.makedirs("새폴더/새폴더1/새폴더2/...", exist_ok=True) #폴더 다수 만들기 폴더가 이미 존재하면 건너뛰기

    # 현재 작업 경로 확인
    print(os.getcwd())

    # 작업 경로 변경 -> 실행할 때 제대로 컴퓨터 구조를 알지 못하면 골치 아픈 상황 발생
    #os.chdir("C:/Users/TJ/OneDrive/바탕 화면")

    # 폴더 안 파일 목록
    print(os.listdir(".")) # 현재 폴더 목록
    print(os.listdir("C:/Users/TJ/OneDrive/바탕 화면")) # 특정 폴더 목록


def 파일작업():
    # 파일/폴더 존재 여부 확인
    os.path.exists("파일이름.확장자") # 결과는 Boolean True / False 나온다.

    # 파일인지 폴더인지
    os.path.isfile("파일이름.확장자") # 파일이면 결과는 True
    os.path.isdir("폴더이름")         # 폴더라면 결과는 True

    # 파일 삭제
    os.remove("파일이름.확장자")

    # 파일이름만 갖고오기
    os.path.basename("폴더1번/폴더2번/폴더3번/파일이름.확장자") # 파일이름.확장자

    # 파일이름과 확장자 분리
    os.path.splitext("파일이름.확장자") # ("파일이름", ".csv")

    os.path.join("폴더1번/폴더2번/폴더3번","파일이름.확장자")












