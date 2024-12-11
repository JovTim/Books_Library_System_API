from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route("/")
def greetings():
    return "<p>Books and Libraries API</p>"

if __name__ == "__main__":
    app.run(debug=True)