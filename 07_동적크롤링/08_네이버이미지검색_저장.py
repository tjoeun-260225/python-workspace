from playwright.sync_api import sync_playwright
import requests # 이미지 다운로드 용
import os       # 이미지 폴더 만들기 용
import time     # 잠시 대기하며 다음 검색을 위한 모듈

# from tests.demo_without_stealth_test import browser, page
# 잘못된 상태 모듈~~~
# ModuleNotFoundError: No module named 'pkg_resources' 보고 싶다면
# page = browser.new_page() 안하면 된다.

def 단일검색():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 이미지 저장할 폴더 만들기
    os.makedirs("다운로드이미지", exist_ok=True) # 폴더가 있으면 스킵 없으면 자동 생성
    # GetMapping("search.naver")
    # public String searchPage(@RequestParam String where, @RequestParam String query = "고양이"){}
    page.goto(f"https://search.naver.com/search.naver?where=image&query=고양이")
    time.sleep(2)

    # 고양이 이미지 데이터 가져오기
    이미지목록 = page.locator("._fe_image_tab_content_thumbnail_image").all()
    print(f"=== 고양이 : {len(이미지목록)}개 발견")

    # for 번호, 이미지한장씩 in enumerate(이미지목록): 전부다 저장
    # for 번호, 이미지한장씩 in enumerate(이미지목록, start=1): start=1 을 작성하지 않으면 번호매김 0번 부터 시작
    for 번호, 이미지한장씩 in enumerate(이미지목록[:5]): # 5개 만 저장
        이미지주소 = 이미지한장씩.get_attribute("src")  # 이미지 태그에서 속성 데이터 가져오기. srt = 이미지 경로 alt = "이미지 없을 때 보여질 별칭 스크린리더"

        if not 이미지주소: # 만약 이미지주소가 없는게 사실이라면
            continue # 건너뛰기~

        try:
            # 이미지가 있다!!!! 시작하자!!! 저장을 !!!!
            응답 = requests.get(이미지주소, timeout=5)

            # 파일로 저장
            #  f" 문 자 열 " 은 print 상관없이 문자열을 작성하는 어디든지 변수+글자를 섞어서 작성할 때 어디서든 사용 가능
            파일이름 = f"다운로드이미지/고양이_{번호+1}.jpg"
            f=open(파일이름, "wb") # wb = 바이너리 쓰기모드 (이미지는 바이너리)
            f.write(응답.content)
            f.close()
            print(f"저장완료 : {파일이름}")
        except:
            print(f"{번호+1}번 이미지 저장 실패")
        time.sleep(2)
    browser.close()
    p.stop()
    print("폴더 이미지 저장 완료")

# 단일검색()
def 다중검색():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 강아지, 토끼, 늑대 3가지
    키워드목록 = ["강아지","토끼","늑대"]

    for 키워드 in 키워드목록:
        # 예: "다운로드이미지/강아지" 형태로 만들어야 합니다
        # 힌트: os.makedirs("???", exist_ok=True)
        저장폴더 = f"다운로드이미지/{키워드}"
        os.makedirs(저장폴더, exist_ok=True)
        page.goto(f"https://search.naver.com/search.naver?where=image&query={키워드}")
        time.sleep(2)
        # class = .속성명칭             id = #.속성명칭     html태그는 특수문자 붙임 없음
        이미지목록 = page.locator("._fe_image_tab_content_thumbnail_image").all()
        print(f"=== {키워드} : {len(이미지목록)}개 발견")
        for 번호, 이미지한장씩 in enumerate(이미지목록):
            이미지주소 = 이미지한장씩.get_attribute("src")

            if not 이미지주소:
                continue

            try:
                응답 = requests.get(이미지주소, timeout=5)
                파일이름 = f"{저장폴더}/{키워드}_{번호+1}.jpg"

                f = open(파일이름, "wb")
                f.write(응답.content)
                f.close()
                print(f"저장완료 : {파일이름}")
            except:
                print(f"{키워드} {번호+1}번 이미지 저장 실패")
        time.sleep(2)

    browser.close()
    p.stop()
    print("전체 이미지 저장 완료!")

다중검색()