import pymysql

def connection():
    conn = pymysql.connect(
        host='',
        user='',
        password='',
        db=''
    )

    return conn