from db_connection import connection
from faker import Faker
import pymysql
import random

fake = Faker()

conn = connection()

"""
bruh meron palang sbn yung faker library 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠐⠀⠈⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢡⣤⣶⣶⣦⢠⣶⣷⣾⠀⢃⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡖⣯⠀⠛⠟⡿⠋⠀⢙⠛⠁⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠸⡅⠈⠀⡰⠳⢶⠖⠰⠀⠀⣏⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠰⢷⣶⣿⠹⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣷⣾⣤⣍⣀⣄⣤⢾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⣿⣿⣻⠛⠻⠟⠋⣼⣯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣄⢤⡖⣪⢕⡮⣝⣿⣿⣿⣿⣿⣿⣿⣶⡌⣸⣿⣿⣿⣓⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢤⠼⣦⣝⢿⣽⢺⡵⣫⣞⡿⣹⠽⣿⣿⣿⣿⣿⣿⣰⣿⣷⣿⣿⣯⣟⢦⡘⣄⣃⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡄⢪⣴⢪⣷⣾⣯⣻⣿⠿⣽⣷⠻⢼⠷⡻⠓⠛⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣽⣲⣭⣷⣸⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡄⢲⣶⢸⣆⡹⢷⣫⣿⣿⣹⣾⣿⣷⣄⢩⣽⢢⡟⣿⣻⢽⣾⣶⡟⢶⣷⣾⣿⣿⣿⡾⣽⣾⣷⣿⣿⣧⡧⡅⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡀⢘⢦⡰⣿⣎⡹⣏⡟⣿⣶⣿⣧⡽⣿⣿⡿⠿⠿⡿⢺⠿⢙⣳⠏⠿⢿⢿⢇⢛⣮⣿⣿⣿⣿⣿⣽⡷⣿⣿⡿⢯⣽⣷⣯⢩⣴⡢⠀⠀⠀⠀⠀⠀
⠀⠀⠠⣖⢮⣿⡾⣻⣴⠻⢿⣎⡻⣿⣽⢿⣯⣹⣿⡷⠦⠈⠀⠀⢘⠀⠀⡀⣀⢄⡐⠠⠬⠨⠷⠠⠀⠹⠝⡛⠓⠛⠟⣿⣿⣿⡿⢷⣼⣿⣎⣁⡄⡑⠄⠀⠀⠀
⢠⣎⣤⣭⡳⢫⢻⣿⣿⣿⣾⣛⣶⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣽⣷⣯⣿⣿⣿⢽⢐⣶⢶⡼⣿⣿⣿⣿⣶⣿⣿⣿⡿⣽⣾⢿⡿⣿⡿⣭⠇⢂⡆⡀⠀
⣩⣝⣛⣒⣻⣿⣷⣮⣟⣷⣿⡟⠟⠉⠀⢹⣿⣿⣿⣿⢭⠤⠍⣀⢉⡊⢈⢢⠀⠀⢂⠐⢀⠶⠿⠘⠈⠩⡉⠻⠟⠿⢟⡏⠉⠻⣿⣿⣿⣏⣿⣷⣿⣿⠿⠶⣾⡄
⢿⣿⢯⣷⢾⣶⣿⣿⣿⣯⡁⠀⠀⠀⠀⠐⣻⣿⣿⣿⣷⣿⣶⣷⣞⣷⣦⣾⣽⣾⣶⣴⠾⣶⢾⠶⡷⢼⣿⣿⣶⣶⣶⡆⠀⠀⠈⢻⣿⣿⡿⣿⡿⣯⣽⣿⣵⠀
⠀⠘⢿⣿⢿⣯⣩⣽⣿⣧⡿⣄⠀⠀⠀⠀⠘⣿⣿⣯⣝⢝⠚⠍⢙⠁⠏⣎⠛⠙⢓⠑⠸⢘⣻⣛⠿⢧⢿⣻⣿⡿⣿⣿⠀⢀⣀⣼⢿⣽⡛⢿⡿⣮⣽⣷⠏⠀
⠀⠀⠀⠙⢾⣽⡿⠿⢿⣩⣿⣟⣙⠄⠀⠀⠀⢽⣿⣿⣿⣴⣿⣾⣾⣿⣺⢾⣿⣿⣷⣎⠪⣉⢰⡀⣤⢷⢾⣶⣴⣦⣤⣴⠾⣿⣿⣿⣮⣭⣵⣮⣽⡿⠟⠀⠀⠀
⠀⠀⠀⠀⠀⠹⢿⣿⣾⣿⣿⣿⣟⢿⣤⠀⠀⠈⣿⣿⡯⠍⠩⠉⡩⣉⢉⢩⠩⠩⠙⠉⠁⣓⣚⣃⠗⠖⠺⢿⢿⣿⣿⣿⣿⣯⣾⢷⣤⢿⣯⠿⠋⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣏⣿⣾⣷⣀⡀⣸⢿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⡏⡝⣍⣿⡈⣇⢰⣠⣦⣶⣦⣦⣤⣼⡿⣇⣿⣿⠏⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣽⣷⣍⡿⠋⠀⠉⠈⠘⣿⣭⠭⠉⠉⣙⠧⣙⢉⡛⢋⠃⠉⠊⠹⠒⠙⡻⠿⠿⡿⣿⣿⣿⣿⣷⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠹⣄⠒⠠⠤⠄⠂⣿⣿⣿⣯⣶⣾⣷⣾⣿⣾⣔⣚⢴⠄⡏⣭⠙⠐⢀⢬⡴⡣⢨⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣤⠀⣼⣿⣯⡍⠍⠀⡊⡈⣌⠀⣟⢁⠏⠠⠐⠸⠛⠿⣉⣩⣾⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⡿⡿⣿⡿⢿⣿⡽⣿⣿⡎⣎⣿⡍⡕⣚⡉⣛⣉⣹⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣭⣂⣶⡰⢶⣔⢶⣀⣦⡆⡄⣠⣈⢻⢻⣻⣿⣱⣼⣺⣵⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⠕⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
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

def insert_author() -> None:
    if conn:
        try:
            cursor = conn.cursor()

            query = """
                    INSERT INTO books_libraries.authors(author_first_name, author_last_name)
                    VALUE(%s, %s)
                    """

            for _ in range(25):
                author_first_name = fake.first_name()
                author_last_name = fake.last_name()
                values = (author_first_name, author_last_name)

                cursor.execute(query, values)
                conn.commit()

                print("Author Record Inserted!")

        except pymysql.MySQLError as e:
            print(f"ERROR: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

def insert_address() -> None:
    if conn:
        try:
            cursor = conn.cursor()

            query = """
                    INSERT INTO books_libraries.addresses(street, city, zip_code, province, country)
                    VALUES(%s, %s, %s, %s, %s)
                    """

            for _ in range(25):
                street = fake.street_address()
                city = fake.city()
                zip = fake.zipcode()
                province = fake.state()
                country = fake.country()
                values = (street, city, zip, province, country)

                cursor.execute(query, values)
                conn.commit()

                print("Address Record Inserted!")

        except pymysql.MySQLError as e:
            print(f"ERROR: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
   #insert_books()
   #insert_author()
   insert_address()