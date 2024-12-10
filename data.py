from db_connection import connection
from faker import Faker
import pymysql
import random

fake = Faker()

conn = connection()

def random_isbn() -> str:
    isbn = random.randint(100, 999)
    country = random.randint(1, 99)
    publisher = random.randint(10, 999)
    title = random.randint(10000, 99999)
    check = random.randint(1, 9)

    return f"{isbn}-{country}-{publisher}-{title}-{check}"

def random_length() -> int:
    length = random.randint(1, 4)
    return length

def insert_books() -> None:
    if conn:
        try:
            cursor = conn.cursor()

            query = """
                    INSERT INTO books_libraries.books (isbn, book_title, date_of_publication)
                    VALUES(%s, %s, %s);
                    """

            for _ in range(25):
                isbn = random_isbn()
                book_title = fake.sentence(nb_words=random_length())
                published_date = fake.date()
                values = (isbn, book_title, published_date)

                cursor.execute(query, values)
                conn.commit()

                print("Books Record Inserted!")

        except pymysql.MySQLError as e:
            print(f"ERROR: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
   insert_books()