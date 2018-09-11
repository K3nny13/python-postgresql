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
        connection = psycopg2.connect(user="rojppsyv", password=getpass.getpass(
        ), database="rojppsyv", host="postgres://rojppsyv:pPn1dzV5YjY7get2UOQewnbjMJjwAGg7@dumbo.db.elephantsql.com:5432")
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO users (email, first_name, last_name) VALUES (%s,%s,%s)",
                           (self.email, self, first_name, self.last_name))
        connection.commit()
        connection.close()
