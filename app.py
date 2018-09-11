from user import User


my_user = User(None, 'rochelle@fake.com', 'Rochelle', "Rossow")
my_user.save_to_db()
print(my_user)
