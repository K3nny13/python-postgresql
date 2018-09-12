from database import Database
from user import User


Database.init(user="postgres", password="postgress", database="postgres", host="localhost")


my_user = User(None, first_name="First", last_name="Last", email="Last@fake.com")
my_user.save_to_db()
print(my_user)
