from user import User


# my_user = User(None, 'rochelle@fake.com', 'Rochelle', "Rossouw")
# my_user.save_to_db()

my_user = User(None, first_name="First", last_name="Last", email="Last@fake.com")
my_user.save_to_db()
print(my_user)
