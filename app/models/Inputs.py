from app import db


class Inputs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dispatcher = db.Column(db.String(15), nullable=False, default='0.0.0.0')
    ipaddress = db.Column(db.String(15), nullable=False, unique=True, default='0.0.0.0')
    ipversion = db.Column(db.Enum('IPv4','IPv6'), nullable=False)
    note = db.Column(db.String(255))

    def __repr__(self):
        return f'<IP adresa: {self.ipaddress}>'