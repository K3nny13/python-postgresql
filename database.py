import psycopg2

def connect():
    return psycopg2.connect(user="postgres", password="postgres",
                                database="postgres", host="localhost") 
