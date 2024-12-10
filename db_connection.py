import pymysql

def connection():
    try:
        conn = pymysql.connect(
            host='',
            user='',
            password='',
            db=''
        )
        print("all good")
        return conn
    except pymysql.MySQLError as e:
        print(f"Error connection {e}")
        return None