from migrate import db

Base = db.Model


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.INTEGER, primary_key=True, unique=True)
    first_name = db.Column('first_name', db.VARCHAR, nullable=False)
    second_name = db.Column('second_name', db.VARCHAR)
    birthday = db.Column('birthday', db.VARCHAR)
    email = db.Column('email', db.VARCHAR(length=345), nullable=False)
    phone_number = db.Column('phone_number', db.VARCHAR(length=50), nullable=False)


class Audience(db.Model):
    __tablename__ = 'audiences'
    id = db.Column('id', db.INTEGER, primary_key=True, unique=True)
    name = db.Column('name', db.VARCHAR, nullable=False)
    user_id = db.Column('user_id', db.INTEGER, db.ForeignKey(User.id), unique=True)
    user = db.relationship("User", backref=db.backref("user"))
    price_for_hour = db.Column('price_for_hour', db.DECIMAL, nullable=False)


class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column('id', db.INTEGER, primary_key=True, unique=True)
    start_time = db.Column('start_time', db.TIMESTAMP, nullable=False)
    end_time = db.Column('end_time', db.TIMESTAMP, nullable=False)
    user_id = db.Column('user_id', db.INTEGER, db.ForeignKey(User.id), unique=True)
    user = db.relationship("User", backref=db.backref("user1"))
    audience_id = db.Column('audience_id', db.INTEGER, db.ForeignKey(Audience.id), unique=True)
    audience = db.relationship("Audience", backref=db.backref("reservation"))



