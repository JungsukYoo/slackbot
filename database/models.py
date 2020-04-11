# models.py
from datetime import datetime
from app import db


class Restaurent(db.Model):
    __tablename__ = 'restaurent'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15))
    address = db.Column(db.String(255))
    create_date = db.Column(db.DateTime, default=datetime.now())
    modify_date = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)


class Restaurent_menu(db.Model):
    __tablename__ = 'restaurent_menu'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    restaurent_id = db.Column(db.ForeignKey('restaurent.id'), index=True)
    menu = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, default=datetime.now())
    modify_date = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)   


def restaurent_all():
    queryset = Restaurent.query.all()
    return queryset

