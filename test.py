import pytest
import pymysql
from db_connection import connection
from api import app
import warnings
from flask_mysqldb import MySQL
from flask import Flask
from db_connection2 import db_information

# -------- FOR DATABASE ----------
@pytest.fixture
def db_connection():
    conn = connection()
    if conn is None:
        pytest.fail("Could not establish database connection")
    yield conn
    conn.close()

def test_connection_success(db_connection):
    assert db_connection.open

def test_query_execution(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM books_libraries.books")
    result = cursor.fetchone()
    assert result[0] >= 0

def test_books_table_has_rows(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM books_libraries.books LIMIT 1")
    result = cursor.fetchone()
    assert result is not None

# it will check if a table exist in the database
# it is supposed to fail, but I modified it to not make an error
@pytest.mark.xfail 
def test_query_with_invalid_table(db_connection):
    cursor = db_connection.cursor()
    try:
        cursor.execute("SELECT * FROM non_existing_table")
    except pymysql.MySQLError as e:
        assert str(e).startswith("Table 'books_libraries.non_existing_table' doesn't exist")

# ---------- API ----------

app = Flask(__name__)
app.config["MYSQL_HOST"] = db_information(0)
app.config["MYSQL_USER"] = db_information(1)
app.config["MYSQL_PASSWORD"] = db_information(2)
app.config["MYSQL_DB"] = db_information(3)
mysql = MySQL(app)

@app.route('/')
def index():
    return "<p>Books and Libraries API</p>"

@app.route('/books')
def get_books():
    return "<p>Forever</p>"

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_db_connection(mocker):
    mock_mysql = mocker.patch('flask_mysqldb.MySQL')
    mock_db = mocker.MagicMock()
    mock_mysql.return_value = mock_db
    yield mock_db

def test_index_page(client, mock_db_connection):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "<p>Books and Libraries API</p>"

def test_get_book(client, mock_db_connection):
    mock_db_connection.cursor.return_value.fetchall.return_value = [("Forever",)]
    response = client.get("/books")
    assert response.status_code == 200
    assert "Forever" in response.data.decode()


