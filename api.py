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

if __name__ == "__main__":
    app.run(debug=True)