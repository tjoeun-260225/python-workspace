'''
데이터를 JSON 처럼 생긴 문서로 저장하는 데이터베이스

엑셀(=일반 DB, MySQL 같은 것)
이름    나이  도시
김개발   25   서울
이몽고   30   부산
행/열이 정해져 있고, 모든 행이 같은 구조여야 한다.

MongoDB
{"name" : "김개발", "age":25, "city":"서울", "hobbies":["코딩","독서"]}
{"name" : "이몽고", "age":30, "sns":{"instagram","@mongo"}}
각 문서가 자기만의 구조를 가질 수 있음, 필드가 달라도 됨
- 미리 테이블 구조를 만들지 않고, 데이터를 그때그때 넣으면된다.
- JSON 형태로 확장 저장 딕셔너리 / 객체 와 구조가 같아서 다루기 편함
- 데이터가 엄~청 많아져도 서버를 늘려서 버틸 수 있다. (구글 페이스북 같은 규모)
- 데이터 구조가 자주 바뀔 때
- SNS  피드, 상품 정보 처럼 항목마다 구조가 다를 때
- 데이터를 빠르게 읽어야 할 때 (데이터 저장보다 조회가 목적일 때)

반대로 회원가입 돈계산 같이 정확해야하는 곳에서는 사용하지 않는다.
nosql 유연함 우선 데이터 일단 저장 조회 빠르게 하자!
rdbms 데이터를 정확히 넣는 것 우선 / 빠른 것보다 제대로 제 자리에 데이터가 들어갔는가?
'''


'''
NoSQL id 는 관계형 데이터베이스에서 제공하는 id 와 다르게 생겼다.
id에 _를 붙여 _id 로 표기하는 이유
MongoDB 자체에서 자동으로 만들어주는 필드이름이다. = _id

 id -> 일반 개발자가 사용하기 위한 필드 명칭
_id -> MongoDB 자체에서 만들고 관리하는 예약어 필드
MongoDB에서 자동으로 관리하는 필드라는 것을 표기하기 위하여 _ 를 붙인 것


69fd55b5      1175f2      46     4544c019
────────      ──────     ────    ─────────
생성시간      기기ID     랜덤    순서번호
타임스탬프
--> 서버가 여러대여도 절대 겹치지 않는 ID를 만들기 위해서 위와 같은 형태로 생성

전체 쿼리 연산자 
비교
$gt     >   초과
$gte    >=  이상
$lt     <   미만
$lte    <=  이하
$eq     ==  같음
$ne     !=  다름
$in         목록 안에 있음
$nin        목록 안에 없음

논리
$and        둘 다 만족
$or         하나라도 만족
$not        조건 반대
$nor        둘 다 아님

배열
$all        모두 포함
$size       배열 길이
$elemMatch  배열 안 조건

필드
$exists     필드 존재 여부

수정
$set        값 변경
$unset      필드 삭제
$inc        숫자 증감
$push       배열 추가
$pull       배열 제거
$addToSet   중복없이 추가


col_books.find({            } , {           }):
                ────────────     ───────────
                     ①               ② 
① 첫 번째 {}  ── 필터조건(어떤 데이터를 가져올 것인가)
                  {             } = 전체 다
                  {"city":"서울"} = 서울 만
                  
                   {"author":"김코딩}, {"title": 1, "price": 1}
                     => SELECT title, price FROM 테이블이름 WHERE author = '김코딩'
                     
                   {"author":"김코딩}, {}   
                     => SELECT * FROM 테이블이름 WHERE author = '김코딩'
                     
                  
① 두 번째 {}  ── 투영(어떤 필드를 보여줄 것인가)
                  0 = 숨기다   1 = 보여주다
                  MongoDB 는 _id를 작성하지 않아도 항상 붙여서 보내줌
                  
                  
                  {}, {"title": 1, "price": 1}    
                     => SELECT _id, title, price FROM 테이블이름
                     =>'_id': ObjectId('69fd55b51175f2464544c01b'), 'title': '자바스크립트 입문', 'price': 22000
                  
                  {}, {"_id": 0, "title": 1, "price": 1} "_id": 0 = id 보여주지마! 
                     => SELECT title, price FROM 테이블이름
                     => 'title': '자바스크립트 입문', 'price': 22000
                  
                  {}, {}
                     => SELECT * FROM 테이블이름
                     => 전부 보여주다. find() 것과 같은 결과로 나온다.
'''


'''
파이썬 환경 세팅
pip install pymongo

설치 확인 방법
pip show pymongo
이름과 버전이 나오면 성공
'''
from pymongo import MongoClient

# 몽고 디비는 27017 포트에서 접속하고 데이터 갖고오기 가능
# client = MongoClient("mongodb://localhost:27017/")['mydb']['users']
client = MongoClient("mongodb://localhost:27017/")


def 몽고디비_파이썬코드_연결확인():
    # 연결 확인
    print("Mongo DB 버전 : ", client.server_info()['version'])  # Mongo DB 버전 :  7.0.32


db = client['mydb']  # 데이터베이스 선택
col = db['users']  # 컬렉션 선택 = 관계형 데이터 베이스 기준 Table 선택


# client / db / col 구분지어서 각 변수 공간에 해당하는 기능에 문제가 있는지 확인하기 위한 작업
# 처리를 위해서 보통은 변수공간에 개별로 세팅
# 문제가 발생할 상황에 대해 예외처리 진행

# 만약 localhost:27017 에서 mydb 데이터베이스에 존재하는 users 컬렉션(=테이블) 내 데이터를
# 모~두 제거한 채 깨긋한 users 컬렉션에서 작업을 하고 싶다면 아래 명령어 주석 해지하고 실행
# col.drop() # 이전 데이터가 존재한다면 모두 초기화

############################### insert ###############################
def insert_저장하기():
    # 한 건 저장
    한건저장결과 = col.insert_one(
        {
            "name": "홍길동",
            "age": 20,
            "city": "경기",
            "tags": ["python", "backend"]
        }
    )
    print("한 건 저장한 결과 확인 : ", 한건저장결과.inserted_id)  # 저장된 id 조회
    # 여러 데이터 저장
    여러건저장결과 = col.insert_many(
        [
            {"name": "김개발", "age": 25, "city": "서울", "tags": ["python", "backend"]},
            {"name": "이몽고", "age": 30, "city": "부산", "tags": ["db", "devops"]},
            {"name": "박클라", "age": 22, "city": "서울", "tags": ["frontend"]},
            {"name": "최데이", "age": 28, "city": "대구", "tags": ["python", "ml"]},
        ]
    )
    print("여러 건 저장한 결과 확인 : ", 여러건저장결과.inserted_ids)  # 다수 데이터 저장된 id들 조회
    '''
    한 건 저장한 결과 확인 :  69fd4e3cea3f84d4888fa076
여러 건 저장한 결과 확인 :  [ObjectId('69fd4e3cea3f84d4888fa077'), ObjectId('69fd4e3cea3f84d4888fa078'), ObjectId('69fd4e3cea3f84d4888fa079'), ObjectId('69fd4e3cea3f84d4888fa07a')]
    '''



def read_조회하기():

    # doc 단순한 변수 이름 document(문서) 줄임말 사용
    # result , data 로 도 많이 사용

    # 한 건 조회 (조건에 맞는 첫 번째)
    doc = col.find_one({"name": "김개발"}) # 조건에 맞는 첫 번째 문서 하나만 갖고온다.
    # 여러 개 있어도 무조건 1개만 반환 없으면 None 반환
    print(f"한건 조회 : {doc}")

    # 전체 조회
    # find() 안에 아무것도 없으면 컬렉션 자체를 갖고옴
    # 갖고온 결과가 여러개므로 for 문으로 하나씩 꺼내서 조회
    # SELECT * FROM users;
    for doc in col.find():
        print(f"전체 조회 : {doc}")

    # 조건 조회 = 도시가 서울인 유저만 조회
    # SELECT * FROM users WHERE city = '서울'
    for doc in col.find({"city": "서울"}):
        print(f"특정 조건만 조회 : {doc}")

    # 정렬 (1 = 오름차순, -1 = 내림차순)
    # SELECT * FROM users ORDER BY age ASC;    .sort("age", 1)
    # SELECT * FROM users ORDER BY age DESC;   .sort("age", -1)
    for doc in col.find().sort("age", 1):
        print("나이 기준 오름차순 정렬 : ", doc)

    # 개수 제한 3개 까지만 조회하기
    # SELECT * FROM users LIMIT 3
    for doc in col.find().limit(3):
        print(f"3개만 조회하기 : {doc}")

    # 특정 필드만 보기(투영)
    # SELECT name, age FROM users
    for doc in col.find({}, {"_id":0, "name":1,"age":1}):
        print(f"특정 필드만  모아보기 : {doc}")

    # 건너 뛰기 (페이지네이션)

    # 1페이지 :  LIMIT 10 OFFSET 0   ->  1번 ~ 10 번 게시물
    # 2페이지 :  LIMIT 10 OFFSET 10  -> 11번 ~ 20 번 게시물
    # 3페이지 :  LIMIT 10 OFFSET 20  -> 21번 ~ 30 번 게시물

    # OFFSET = 여기서부터 시작할게 앞에것은 무시하자!

    # SELECT * FROM users LIMIT 3 OFFSET 2
    # OFFSET = 앞에 몇 개 건너뛰고 조회할지 선택
    # LIMIT 3 OFFSET 2 = 앞에 2개 건너뛰고, 그 다음부터 3개만 가져와서 조회하겠다.
    for doc in col.find().skip(2).limit(3):
        print(f"건너뛰기 : ", doc)

    #개수 세기
    count = col.count_documents({"city":"서울"})
    print(f"도시가 서울인 인원 수 : {count}")

    # 존재 여부 확인
    exists = col.find_one({"name":"김개발"}) is not None
    print(exists)

read_조회하기()
