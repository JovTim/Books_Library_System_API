import pymysql

def connection():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='T1m0s@99145078',
            db='books_libraries'
        )
        print("all good")
        return conn
    except pymysql.MySQLError as e:
        print(f"Error connection {e}")
        return None