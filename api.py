from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL
from db_connection2 import db_information

import jwt
import datetime
from functools import wraps

from api_key import api_key



#from data_generator.data import random_isbn

app = Flask(__name__)
app.config["MYSQL_HOST"] = db_information(0)
app.config["MYSQL_USER"] = db_information(1)
app.config["MYSQL_PASSWORD"] = db_information(2)
app.config["MYSQL_DB"] = db_information(3)

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

STATIC_TOKEN = api_key()


mysql = MySQL(app)

@app.route("/")
def greetings():
    return "<p>Books and Libraries API</p>"

# ------------ TOKEN -----
def validate_token():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'message': 'Token is missing!'}), 403

    token_data = token.split(" ")[1] 

    if token_data == STATIC_TOKEN:
        return True
    else:
        return jsonify({'message': 'Invalid token!'}), 401
# -----------------------

# --------------- account and data validation -------------
    
def validate_request_data(required_fields):
    info = request.get_json()
    if not info:
        return jsonify({"message": "Invalid JSON payload!"}), 400
    
    if not all(field in info for field in required_fields):
        return jsonify({"Message": f"Missing required fields: {required_fields}"}), 400
    
    return info


def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    return data
# ----------------BOOK REQUEST------------------------
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
# ----------------------------------------------

# ---------------BOOKS MANAGEMENT--------------

@app.route("/books", methods=["GET"])
def get_books() -> None:
    cur = mysql.connection.cursor()
    query = """
            SELECT books.book_id, books.isbn, books.book_title, books.date_of_publication, categories.category_name, books.author_name
            FROM books_libraries.books as books
            INNER JOIN books_libraries.categories as categories
            ON categories.category_id = books.category_id;
            """
    
    data = data_fetch(query)

    return make_response(jsonify(data), 200)

@app.route("/books/<int:id>", methods=["GET"])
def get_book_by_id(id: int):
    query = """
            SELECT books.book_id, books.isbn, books.book_title, books.date_of_publication, categories.category_name, books.author_name
            FROM books_libraries.books as books
            INNER JOIN books_libraries.categories as categories
                ON categories.category_id = books.category_id
            WHERE books.book_id = {};
            """.format(id)
    
    data = data_fetch(query)

    return make_response(jsonify({"books.book_id": id, "count": len(data), "information": data}), 201)

@app.route('/book', methods=['POST'])
def add_book():
    cur = None 
    try:
        # Validate the token
        token_validation = validate_token()
        if token_validation is not True:
            return token_validation 

        # Validate the book data
        required_fields = ["isbn", "book_title", "date_of_publication", "category_id", "author_name"]
        validation_result = validate_request_data(required_fields)
        if isinstance(validation_result, dict):
            info = validation_result
        else:
            return validation_result 

        cur = mysql.connection.cursor()
        isbn = info["isbn"]
        book_title = info["book_title"]
        date_of_publication = info["date_of_publication"]
        category_id = info["category_id"]
        author_name = info["author_name"]

        query = """
            INSERT INTO books_libraries.books(isbn, book_title, date_of_publication, category_id, author_name)
            VALUES(%s, %s, %s, %s, %s);
        """
        values = (isbn, book_title, date_of_publication, category_id, author_name)
        cur.execute(query, values)
        mysql.connection.commit()

    except Exception as e:
        print(f"Error: {e}")
        if cur:
            mysql.connection.rollback()
        return jsonify({'message': 'An error occurred while adding the book'}), 500

    finally:
        if cur:
            print("row(s) affected: {}".format(cur.rowcount))
            rows_affected = cur.rowcount
            cur.close()
        else:
            rows_affected = 0

    return make_response(jsonify({"message": "Book added successfully", "row_affected": rows_affected}), 201)

@app.route('/book/<int:id>', methods=["PUT"])
def edit_book(id: int) -> None:
    ...

@app.route("/book/<int:id>", methods=["DELETE"])
def delete_book(id: int) -> None:
    ...
# --------------------------------------------

# --------------LIBRARY MANAGEMENT------------
@app.route("/library", methods=["GET"])
def get_libraries() -> None:
    ...

@app.route("/library/<int:id>/details", methods=["GET"])
def get_library_details(id: int) -> None:
    ...

@app.route("/library", methods=["POST"])
def add_library() -> None:
    ...

@app.route("/library/<int:id>", methods=["PUT"])
def edit_library(id: int) -> None:
    ...

@app.route("/library/<int:id>", methods=["DELETE"])
def delete_library(id: int) -> None:
    ...

if __name__ == "__main__":
    app.run(debug=True)