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

def insert_category() -> None:
    if conn:
        try:
            book_categories = [
                "fiction",
                "non-fiction",
                "mystery",
                "fantasy",
                "science fiction",
                "biography",
                "romance",
                "history",
                "self-help",
                "children's literature",
                "poetry",
                "thriller",
                "adventure",
                "cookbooks",
                "graphic novels"
            ]
            cursor = conn.cursor()

            query = """
                    INSERT INTO books_libraries.categories(category_name)
                    VALUES(%s);
                    """

            for i in book_categories:
                cursor.execute(query, i)
                conn.commit()

                print("Category Record Inserted!")

        except pymysql.MySQLError as e:
            print(f"ERROR: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

def insert_member() -> None:
    if conn:
        try:
            cursor = conn.cursor()

            query = """
                    INSERT INTO books_libraries.members(member_address_id, gender, first_name, last_name, phone_number, email_address)
                    VALUES(%s, %s, %s, %s, %s, %s);
                    """
# member_address_id, gender, first_name, last_name, phone_number, email_address
            for i in range(26):
                address_id = random.randint(1, 26)
                gender = random.randint(0, 1)
                first_name = fake.first_name()
                last_name = fake.last_name()
                phone_number = fake.phone_number()
                email_address = fake.email()
                values = (address_id, gender, first_name, last_name, phone_number, email_address)

                cursor.execute(query, values)
                conn.commit()

                print("Members Record Inserted!")

        except pymysql.MySQLError as e:
            print(f"ERROR: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

def insert_library() -> None:
    if conn:
        try:
            cursor = conn.cursor()

            query = """
                    INSERT INTO books_libraries.libraries(address_id, library_name, library_details)
                    VALUES(%s, %s, %s)
                    """
# address_id, library_name, library_details
            for i in range(26):
                address_id = random.randint(1, 26)
                library_name = f"{fake.company()} library"
                library_details = fake.sentence(nb_words=10)
                values = (address_id, library_name, library_details)

                cursor.execute(query, values)
                conn.commit()

                print("library Record Inserted!")

        except pymysql.MySQLError as e:
            print(f"ERROR: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
def insert_books_by_category() -> None:
    if conn:
        try:
            cursor = conn.cursor()

            query = """
                    INSERT INTO books_libraries.books_by_category(category_id, book_id)
                    VALUES(%s, %s)
                    """
# category_id, book_id
            for i in range(1, 26):
                category = random.randint(1, 16)
                values = (category, i)

                cursor.execute(query, values)
                conn.commit()

                print("books_by_category Record Inserted!")

        except pymysql.MySQLError as e:
            print(f"ERROR: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

def insert_member_request() -> None:
    if conn:
        try:
            cursor = conn.cursor()

            query = """
                    INSERT INTO books_libraries.member_request(member_id, book_id, date_requested, date_located, other_request)
                    VALUES(%s, %s, %s, %s, %s)
                    """
# member_id, book_id, date_requested, date_located, other_request
            for _ in range(26):
                member_id = random.randint(1, 26)
                book_id = random.randint(1, 26)
                date = fake.date()
                other_request = fake.sentence(nb_words=10)
                values = (member_id, book_id, date, date, other_request)

                cursor.execute(query, values)
                conn.commit()

                print("member_request Record Inserted!")

        except pymysql.MySQLError as e:
            print(f"ERROR: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
   #insert_books()
   #insert_author()
   #insert_address()
   #insert_category()
   #insert_member()
   #insert_library()
   #insert_books_by_category()
   insert_member_request()