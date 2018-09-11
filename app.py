from user import User


my_user = User('kenny@fake.com', 'Kenny', "Cogzell", None)
my_user.save_to_db()
print(my_user)
