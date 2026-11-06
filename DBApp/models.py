# from DBApp.app1 import db

# class Person(db.Model):
#     __tablename__ = 'people'

#     p_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text, nullable=False)
#     age = db.Column(db.Integer)
#     job = db.Column(db.Text)

#     def __repr__(self):
#         return f"Person with name {self.name} and age {self.age}"



from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<User {self.username} - Role {self.role}>"

    def get_id(self):
        return str(self.uid)