import mysql.connector # pip install mysql-connector-python 으로 설치한 것
# 이 것을 가져와야 MySQL 연결 가능
'''
db:
  url: jdbc:mysql://localhost:3306/instagram_clone
  username: root
  password: tjee1234
'''
def DB연결():
    conn = mysql.connector.connect(
        host="localhost",               # 어느 컴퓨터에 있는 DB localhost = 내컴퓨터
        port=3306,                      # MySQL 접속 번호 python에서 3306 로 접속해서 DB 가져온다.
        user="root",                    # DB 아이디
        password="tjee1234",            # DB 비밀번호
        database="instagram_clone"      # 데이터를 가져오고 수정하고 삭제할 DB 지정
    )
    return conn # 위 모든 상태를 conn에 담아서 반환하겠다.
def 유저전체조회기능():
    conn = DB연결()
    #cursor = conn.cursor()
    cursor = conn.cursor(dictionary=True) # dictionary 형태로 출력을 할 수 있다.
    cursor.execute("SELECT * FROM users")
    결과목록 = cursor.fetchall()
    for 행 in 결과목록:
        print(행)
    cursor.close()
    conn.close()

유저전체조회기능()