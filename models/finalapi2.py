import sqlite3

from d import db



class UserModel(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80))
    password=db.Column(db.String(90))
    def __init__(self,  username, password):


        self.username = username
        self.password = password

    @classmethod
    def finding_name(cls, username):
        return UserModel.query.filter_by(username=username).first()

    @classmethod
    def finding_id(cls, id):
        return UserModel.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



