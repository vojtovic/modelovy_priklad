from app import db


class Dispatcher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    ipaddress = db.Column(db.String(15), nullable=False, unique=True, default='0.0.0.0')
    
    def __repr__(self):
        return f'<IP adresa: {self.ipaddress}>'