from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL
from db_connection2 import db_information

app = Flask(__name__)
app.config["MYSQL_HOST"] = db_information(0)
app.config["MYSQL_USER"] = db_information(1)
app.config["MYSQL_PASSWORD"] = db_information(2)
app.config["MYSQL_DB"] = db_information(3)

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def greetings():
    return "<p>Books and Libraries API</p>"

def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    return data

@app.route("/member_requests", methods=["GET"])
def get_member_request() -> None:
    cur = mysql.connection.cursor()
    query = """
            SELECT members.member_id,members.first_name, members.last_name, books.book_title,member_request.date_requested
            FROM books_libraries.members as members
            INNER JOIN books_libraries.member_request as member_request
                ON member_request.member_id = members.member_id
            INNER JOIN books_libraries.books as books
                ON member_request.book_id = books.book_id
            """
    
    data = data_fetch(query)

    return make_response(jsonify(data), 200)

#member_id, book_id, date_requested, date_located, other_request
@app.route("/member_request", methods=["POST"])
def add_book_request() -> None:
    try:
        cur = mysql.connection.cursor()
        info = request.get_json()
        member_id = info["member_id"]
        book_id = info["book_id"]
        date_requested = info["date_requested"]
        date_located = info["date_located"]
        other_request = info["other_request"]

        query = """
                INSERT INTO books_libraries.member_request(member_id, book_id, date_requested, date_located, other_request)
                VALUES(%s, %s, %s, %s, %s)
                """
        values = (member_id, book_id, date_requested, date_located, other_request)
        cur.execute(query, values)
        mysql.connection.commit()
    except:
        print("Error")
        mysql.connection.rollback()
    finally:
        print("row(s) affected: {}".format(cur.rowcount))
        rows_affected = cur.rowcount
        cur.close()
        return make_response(jsonify({"message": "book request added successfully", "row_affected": rows_affected}))

    

if __name__ == "__main__":
    app.run(debug=True)