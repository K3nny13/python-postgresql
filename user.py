import psycopg2
import getpass


class User:
    def __init__(self, id, email, first_name, last_name):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        connection = psycopg2.connect(user="postgres", password=getpass.getpass(
        ), database="postgres", host="localhost")
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO users (first_name, last_name, email) VALUES (%s,%s,%s)",
                           (self.first_name, self.last_name, self.email))
        connection.commit()
        connection.close()
