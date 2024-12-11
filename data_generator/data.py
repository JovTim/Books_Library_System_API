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


def insert_books_at_libraries() -> None:
    if conn:
        try:
            cursor = conn.cursor()

            query = """
                    INSERT INTO books_libraries.books_at_libraries(library_id, book_id, quantity_in_stock)
                    VALUES(%s, %s, %s)
                    """
# library_id, book_id, quantity_in_stock
            for i in range(1, 26):
                random_books = random.randint(4, 26 + 1)
                for j in range(1, random_books):
                    library_id = i
                    quantity_in_stock = random.randint(0, 99)
                    values = (library_id, j, quantity_in_stock)

                    cursor.execute(query, values)
                    conn.commit()

                    print("books_at_libraries Record Inserted!")

        except pymysql.MySQLError as e:
            print(f"ERROR: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

def update_books() -> None:
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                    UPDATE books_libraries.books
                    SET category_id = %s,
                    author_name = %s
                    WHERE book_id = %s
                    """
            
            for i in range(1, 26):
                category_id = random.randint(1, 16)
                author_name = fake.name()
                values = (category_id, author_name, i)
                
                cursor.execute(query, values)
                conn.commit()
                print("books updated!")

        except pymysql.MySQLError as e:
            print(f"ERROR: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
   #insert_books()
   #insert_address()
   #insert_category()
   #insert_member()
   #insert_library()
   #insert_member_request()
   #insert_books_at_libraries()
   #update_books()
   ...