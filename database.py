from database import pool


connection_pool = pool.SimpleConnectionPool(1 , 10, user="postgres", password="postgres",
                                database="postgres", host="localhost")

 
