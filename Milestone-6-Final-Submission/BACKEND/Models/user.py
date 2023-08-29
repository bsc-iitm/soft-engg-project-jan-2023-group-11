import enum
from sqlalchemy.types import Enum

from db import db
from .creater import creater
from .solver import solver

class UserType(str, enum.Enum):
    ADMIN = 'ADMIN'
    STUDENT = 'STUDENT'
    SUPPORT_STAFF = 'SUPPORT_STAFF'


class User(db.Model) :

    __tablename__ = 'user'

    _id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    usertype = db.Column(Enum(UserType))

    created_tickets = db.relationship('Ticket', secondary=creater, lazy='subquery', backref='created_user')
    solved_ticket = db.relationship('Ticket', secondary=solver, lazy='subquery', backref='solved_user')

    def __init__(self, username, password, usertype):
        
        self.username = username
        self.password = password


        if usertype == 'ADMIN' :
            self.usertype = UserType.ADMIN

        if usertype == 'STUDENT' :
            self.usertype = UserType.STUDENT
        
        if usertype == 'SUPPORT_STAFF' :
            self.usertype = UserType.SUPPORT_STAFF
        

    
    def add_user(self) :

        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_user_by_id(cls, _id) :
        return cls.query.filter_by(_id = _id).first()

    @classmethod
    def get_user_by_username(cls, username) :
        return cls.query.filter_by(username =  username).first()  
    
    



    
    