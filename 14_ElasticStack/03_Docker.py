'''
Docker = dock(항구 부두) + er(하는 것)

컨테이너에서 아이디어를 가져온 것

개념
이미지(Image)
- 설치 설명서 + 재료 묶음
- springboot:3.4.5 이미지 = 스프링부트 3.4.5 를 실행하는데 필요한 모든 것이 담긴 패키지

컨테이너(Container)
- 이미지를 실제로 실행한 공간
- 이미지 하나로 컨테이너 무수히 만들 수 있다.

엘라스틱서치 / 엘라스틱스택은 도커를 이용해서 사용
엘라스틱서치 자체를 나의 컴퓨터에 맞추어 설치하려면 매우 까다로움
버전관리가 용이 / 여러 도구를 같이 사용

docker-compose_flask.yml
- 여러 Docker 컨테이너를 한 번에 정의 하고 실행하는 설정 파일

-- 만약 도커 컴포즈 파일을 이용하지 않는다면
-- cmd 명령 프로프트 창에
docker run -d --name es01 --e discovery.type=signle-node 식으로 수기로 모든세팅을 작성해야한다.
'''
"""
하나의 컴포즈 파일 실행 방법
docker compose up -f 파일이름.yml  -d
docker compose up -f 파일이름.yaml -d

여러 파일 동시에 사용도 가능
docker compose up -f 파일이름1.yml -f 파일이름2.yaml -f 파일이름3.yaml -d

도커 명령어
docker compose up -d   # 컨테이너 생성 + 시작
docker compose down    # 컨테이너 중지 + 삭제
docker compose stop    # 컨테이너 중지만 삭제하지 않는다.
docker compose start   # 중지된 컨테이너 재시작
docker compose ps      # 실행중인 컨테이너 목록
docker compose logs -f # 컨테이너에서 어떤 작업이 되고 있는지 기록보기
docker compose restart # 컨테이너 재부팅

docker-compose_flask.yml 기본 코드
services:
    web:
        image:사용할 모듈 경로 / 이름
        port : 도커와 나의 개발 컴퓨터와 연결할 번호 설정 
            - "8080:80"  외부포트:내부포트
    db:
        image: 사용할 모듈 경로 / 이름:버전
        port : 도커와 나의 개발 컴퓨터와 연결할 번호 설정 
            - "8080:80"  외부포트:내부포트
image = 라이브러리, 프레임워크, 모듈마다 필요한 속성을 표기한다.
"""
'''
도커는 언제 사용하는가
= 내 컴퓨터에서 잘 동작해서 고객사에 코드 제품을 납품했는데
고객사에서 안돼요. 를 없애기 위해서 사용

1. 개발 환경을 통일할 때 ( RAM 이나 SSD 와 같이 컴퓨터 부품에는 이상없다는 전제하)
 -- 팀원 A 는 Mac, B 는 Windows, 서버는 Linux 
    -> 도커 사용하면 각 컴퓨터 환경을 알 필요 없이 개발한 후 도커  파일 제공
       docker-compose.yaml 을 제공하면 컴퓨터 os 환경에 관계없이 실행 가능
       
2. 서버에 배포할 때
 -- docker에서 image 하나로 묶어서 서버에서 사용할 수 있다.
 
3. 여러 서비스를 한 컨테이너에서 동시에 띄우고 종료할 때
 -- service:
        web:
        api:
        db:
        redis:
    --> docker compose up -d 명령어 하나로 4개 동시 실행 가능
    
4. 테스트 환경을 빠르게 만들고 지우고 싶을 때
 -- docker run mysql:8.0 #  mysql만 즉시 실행
 -- docker compose down  #  흔적 없이 삭제
 
5. 하나의 언어에서 여러 버전을 동시에 사용해야 할 때
docker run python:3.8 ...
docker run python:3.12 ...
하나의 컴퓨터에서 다수 버전 동시 사용 가능

도커 = 내 개발 환경을 박스째로 포장해서 어디든 문제없이 똑같이 실행하는 박스
'''