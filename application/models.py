from application import db

class Base(db.Model):

    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    luotu = db.Column(db.DateTime, default=db.func.current_timestamp())