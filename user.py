from database import CursorFromConnectionFromPool


class User:
    def __init__(self, id, email, first_name, last_name):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
			cursor.execute("INSERT INTO users (first_name, last_name, email) VALUES (%s,%s,%s)",
							(self.first_name, self.last_name, self.email)) # second arguement must be a tuple
        # connection.commit() -- 'with' automatically .commits() and .close() when closed
        # connection.close()

    @classmethod
    def load_from_db_by_email(cls, email):
		with CursorFromConnectionFromPool() as cursor:
			cursor.execute('SELECT * FROM users WHERE email=%s', (email,)) # second arguement must be a tuple
			user_data = cursor.fetchone()
			return cls(id=user_data[0], email=user_data[3], first_name=user_data[1], last_name=user_data[2])

