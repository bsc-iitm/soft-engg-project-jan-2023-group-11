from db import db

creater = db.Table('creater',
    db.Column('user_id', db.Integer, db.ForeignKey('user._id'), primary_key=True),
    db.Column('ticket_id',db.Integer, db.ForeignKey('ticket.ticket_id'),primary_key=True)
)