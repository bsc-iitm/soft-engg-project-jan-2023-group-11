from db import db
from datetime import datetime                   
import pytz
import enum
from sqlalchemy.types import Enum
from Models.user import User

class Category(str,enum.Enum) :

    PYTHON = "PYTHON"
    OPERATIONAL = "OPERATIONAL"
    SOFTWARE_ENGINEERING = "SOFTWARE_ENGINEERING"
    MACHINE_LERANING = "MACHINE_LEARNING"
    OTHERS = "OTHERS" 


class Ticket(db.Model) :

    __tablename__ = 'ticket'

    ticket_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category = db.Column(Enum(Category), nullable=False)
    title = db.Column(db.String, nullable=False)
    _query = db.Column(db.String, nullable=False)
    solution = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Kolkata')))
    solved_at = db.Column(db.DateTime, nullable=True)
    is_resolved = db.Column(db.Boolean, default=False, nullable=False) 
    is_faq = db.Column(db.Boolean, default=False, nullable=False) 
    pin = db.Column(db.Boolean, default=False, nullable=False) 
    report = db.Column(db.Boolean, default=False, nullable=False) 
    likes = db.Column(db.Integer, default=0, nullable=False)


    def __init__(self, title, query, category):
        
        self._query = query
        self.title = title
        
        if category == 'PYTHON' :
            self.category = Category.PYTHON
        
        elif category == 'OPERATIONAL' :
            self.category = Category.OPERATIONAL
        
        elif category == 'SOFTWARE_ENGINEERING' :
            self.category = Category.SOFTWARE_ENGINEERING

        elif category == 'MACHINE_LEARNING' :
            self.category = Category.MACHINE_LERANING
        else :
            self.category = Category.OTHERS

        

    def create_query(self) :
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_ticket_by_id(cls, ticket_id) :
        # print(ticket_id)
        return cls.query.filter_by(ticket_id=ticket_id).first()
    
    @classmethod
    def get_all_ticket(cls):
        return cls.query.all()
    
    @classmethod
    def get_ticket_by_category(cls, category) :
        
        if category == 'PYTHON' :
            category = Category.PYTHON
        
        elif category == 'OPERATIONAL' :
            category = Category.OPERATIONAL
        
        elif category == 'SOFTWARE_ENGINEERING' :
            category = Category.SOFTWARE_ENGINEERING

        elif category == 'MACHINE_LEARNING' :
            category = Category.MACHINE_LERANING
        else :
            category = Category.OTHERS

        return cls.query.filter_by(category=category).all()

    
    

        
    

    

