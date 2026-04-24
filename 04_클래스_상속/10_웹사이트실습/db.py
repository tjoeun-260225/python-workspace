import mysql.connector

def DB연결():
    conn = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="tjee1234",
        database="instagram_clone"
    )
    return conn


