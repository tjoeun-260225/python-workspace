from db import DB연결

class 상품서비스:
    def __init__(self):
        self.conn = DB연결()

    def 전체조회(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()

    def 상세조회(self, id):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
        return cursor.fetchone()