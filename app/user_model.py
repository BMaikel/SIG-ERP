from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
    
    def is_authenticated(self):
        if self.username is not None and self.password is not None:
            return True
        else:
            return False

    def get_id(self):
        return str(self.id)

    def is_admin(self):
        if self.username == "admin":
            return True