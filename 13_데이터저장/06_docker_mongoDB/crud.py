from pymongo import MongoClient

# 연결                                         mongoDB   RDB     elasticsearch
#                                              컬렉션 = 테이블 = 인덱스
#                                                             /데이터베이스이름
클라이언트 = MongoClient("mongodb://admin:password@localhost:27017/")
"""
ports:
  - "27017:27017"
environment:
  MONGO_INITDB_ROOT_USERNAME: admin
  MONGO_INITDB_ROOT_PASSWORD: password
"""
데이터베이스 = 클라이언트["mydb"]
컬렉션 = 데이터베이스["users"]


# INSERT
def 저장하기():
    user = {"name": "홍길동", "age": 30, "email": "hong@email.com"}
    result = 컬렉션.insert_one(user)
    print("저장된 id : ", result.inserted_id)  # 저장된 id 확인


# SELECT
def 조회하기():
    # 전체 조회
    for user in 컬렉션.find():
        print("하나씩 조회 : ", user)

    # 조건 조회   컬렉션 = 데이터베이스["users"]                    {}   데이터베이스["users"]              {"name":"홍길동"}
    # user = 컬렉션.find_one({}, {"name": "홍길동"})  # select   *            from users                where name = '홍길동'
    user = 컬렉션.find_one( {"name": "홍길동"})  # select   *            from users                where name = '홍길동'
    print("이름이 홍길동인 유저 맨 첫 번째에 발견한 하나 조회 : ", user)


# UPDATE
def 수정하기():
    result = 컬렉션.update_one(
        {"name": "홍길동"},  # 조건
        {"$set": {"age": 31}}  # $set 변경할 컬럼에서 변경데이터 작성
    )
    print("수정된 컬럼 개수 결과: ", result.modified_count)  #


# DELETE
def 삭제하기():
    result = 컬렉션.delete_one({"name": "홍길동"})
    print("삭제된 데이터 수 : ", result.deleted_count)

# crud 를 import 했다해서 모든 기능을 수행하지 못하도록 설정
if __name__ == "__main__": # import crud 한 py 파일에서 crud.저장하기() 와 같이 기능을 호출하지 않으면 사용 불가
    저장하기()
    조회하기()
    수정하기()
    삭제하기()



"""
Authentication failed., 
full error: {'ok': 0.0, 'errmsg': 'Authentication failed.', 'code': 18, 'codeName': 'AuthenticationFailed'}
기존 컨테이너에 다른 인증 정보가 표기된다.

"""
