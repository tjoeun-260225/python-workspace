import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 이미지를 저장할 폴더 생성
SAVE_DIR = "dog" # 저장할 폴더 명칭
os.makedirs(SAVE_DIR, exist_ok=True)

크롬옵션 = Options()
크롬옵션.add_argument("--start-maximized")
드라이버 = webdriver.Chrome(options=크롬옵션)

try:
    # 네이버에서 검색을 했을 때 접속하는 공통주소  클라이언트가 클릭하는 대로 변경되어 보여질 페이지
    #                                                  탭클릭         이미지검색  탭클릭해서이동   검색어
    # https://search.naver.com/search.naver       ?ssc=tab.image.all&where=image&sm=tab_jum        &query=강아지
    #                                               블로그탭클릭
    # https://search.naver.com/search.naver       ?ssc=tab.blog.all             &sm=tab_jum        &query=강아지
    # https://search.naver.com/search.naver       ?ssc=tab.cafe.all             &sm=tab_jum        &query=강아지
    url="https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query=강아지"
    드라이버.get(url)

    time.sleep(3) # 크롤링 할 것인데 너무 빠르면 임시 차단이 되므로 3초간 쉰다 사람처럼

    # 나는 변수에 담아서 무언가 할 건 아니지만 10번은 아래 기능을 해야겠어 할 때 사용
    for _ in range(10): # 아래 기능을 10번정도 하기 위한 트릭
        드라이버.execute_script(
            # 자바스크립트 기능을 이용해서 화면 맨 아래까지 스크롤 내리겠다.
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        # 너무 빠르면 차단당하니 2초씩 쉬면서 마치 사람이 스크롤 내리는 듯한 효과 제공
        time.sleep(2)

    # 현재 페이지에 존재하는 모든 이미지 태그 가져오기
    이미지들 = 드라이버.find_elements(By.TAG_NAME, "img")

    이미지_주소들 = set() # 중복이 있는 이미지는 제거
    """
    list = 일반 늘어나고 줄어들 수 있는 목록, 리스트
          0번부터 순차적으로 데이터 저장이되며, 0과 같은 숫자로 데이터 위치가 구분되므로
          데이터값 중복 저장 가능
    dict(=map) = 키 값 형태로 데이터 저장
                키 명칭은 중복이 될 수 없지만, 값은 중복 가능
                철수:20,
                영희:20 가능
                
                철수:20,
                철수:22    철수 20에서 22로 마지막에 작성한 값으로 교체
    set = 데이터가 중구난방으로 존재, 순번이 존재하거나 키가 존재하지 않아
          내부에서는 데이터가 중복으로 존재할 수 없다.
          보통 리스트에서 중복을 제거할 때 많이 사용
    """

    for 이미지 in 이미지들:
        src속성=(
            # <img 태그 내에 이미지 주소 속성이 src=""  또는 data-src="" 또는 "data-lazy-src"
            # 세 가지를 순차적으로 존재하는지 확인하고 갖고오기
            # 1. src 에 없으면 2. data-src 없으면 3. data-lazy-src 존재하는지 확인
            이미지.get_attribute("src")
            or 이미지.get_attribute("data-src")
            or 이미지.get_attribute("data-lazy-src")
        )
        # 위에서 가져온 이미지 경로가 http로 시작하는게 맞다면
        if src속성 and src속성.startswith("http"):
            이미지_주소들.add(src속성) # 나중에 이미지 가져올 이미지_주소들 리스트에
            # 현재 http 경로를 추가해놓겠다.

        print(f"수집된 이미지 url 수 : {len(이미지_주소들)}")
    #================ 우리가 가져올 이미지를 위해서 탐색 ===================
    #============ 본격적으로 이미지를 가져와서 내 컴퓨터에 저장 ============
    # 이미지에 순번을 매겨 저장
    count = 1
    # 사람인척 위장하고 데이터 수집
    # 컴퓨터에게 다른 사이트를 들어가서 무언가를 시킬 때 사람이다 라는 표기를 해주지 않으면
    # 나는 파이썬 코드이고 웹사이트를 방문했어 와 같이 표기를 하고 웹사이트 방문

    headers = {
        #나는 사람이고
        "User-Agent":(
            # 웹으로 마우스를 클릭해서 윈도우컴퓨터로 해당 사이트에 접속했어
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            # 크롬이라는 회사에서 사용하는 사이트 여는 엔진 중 하나 명칭일 뿐
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            # 크롬 버전과 safari 호환성표기법 실제 사파리는 아니다.
            "Chrome/137.0 Safari/537.36"
        )
    }

    for 이미지_주소 in 이미지_주소들:
        try:
            응답 = requests.get(
                이미지_주소, # 가져올 이미지를 하나씩 꺼내서
                headers=headers, # 사람인척 위장하고
                timeout=10,     # 이미지 하나당 10초 이내 응답 없으면 포기하고
                # 다음 이미지 주소로 접속해서 데이터  가져올 준비하겠다.
            )
            if 응답.status_code == 200:
                파일이름 = os.path.join(
                    SAVE_DIR,
                    f"dog_{count}.jpg"
                ) # dog/dog_1.jpg 와 같은 형태로 이미지를 저장할 이름만 만들기

                # with = 파일 열고 닫기 자동으로 해줌
                # "w" = 글자만 덮어쓰기 "r" = 글자만 읽기모드 "wb" = 파일 생성 "rb" = 파일 읽기
                with open(파일이름, "wb") as f:
                    f.write(응답.content)

                print(f"저장완료 : {파일이름}")
                count += 1 # 다음 강아지 이미지 번호 +1 증가

        except Exception as e:
            print("다운로드 실패 : ",e)

finally:
    드라이버.quit() # 크롬창 닫기






