from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["library"]          # mydb 말고 library DB 새로 만들기
col_members = db["members"]     # 회원 컬렉션
col_books = db["books"]         # 도서 컬렉션
col_loans = db["loans"]         # 대출 컬렉션

'''
컬렉션명: members

필드명:
- name        (이름)
- age         (나이)
- city        (도시)
- grade       (등급)
- tags        (관심분야 배열)

insert_one 으로 1명 저장:
name:"홍길동" / age:28 / city:"서울" / grade:"일반" / tags:["소설","역사"]

insert_many 로 4명 저장:
name:"김도서" / age:35 / city:"부산" / grade:"VIP"  / tags:["IT","자기계발"]
name:"이열람" / age:22 / city:"서울" / grade:"일반" / tags:["소설","만화"]
name:"박반납" / age:41 / city:"대구" / grade:"VIP"  / tags:["역사","철학"]
name:"최연체" / age:19 / city:"서울" / grade:"정지"] / tags:["만화"]

조건: inserted_id, inserted_ids 출력

컬렉션명: books

필드명:
- title       (제목)
- author      (저자)
- price       (가격)
- pub_year    (출판연도)
- stock       (재고)
- tags        (장르 배열)

insert_many 로 한 번에 저장:
"파이썬 기초"        / "김코딩"  / 25000 / 2024 / stock:5  / tags:["IT","프로그래밍"]
"세계사 한눈에"      / "이역사"  / 18000 / 2023 / stock:3  / tags:["역사","교양"]
"자바스크립트 완전정복" / "박프론트" / 32000 / 2025 / stock:2  / tags:["IT","프로그래밍"]
"철학의 시작"        / "최철학"  / 21000 / 2022 / stock:7  / tags:["철학","교양"]
"만화로 보는 과학"   / "정만화"  / 15000 / 2024 / stock:10 / tags:["만화","과학"]

조건: inserted_ids 출력

'''