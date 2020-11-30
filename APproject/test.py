from models import *
import datetime

user = User(first_name='user', second_name='user', birthday='14.08.2002', email='example@gmail.com', phone_number='0983485535')
audience = Audience(name='audience', price_for_hour='100', user=user)
reservation = Reservation(start_time=datetime.datetime(2020, 11, 29, 12, 30), end_time=datetime.datetime(2020, 11, 29, 14, 30), user=user, audience=audience)

# db.create_all()

db.session.add(user)
db.session.add(audience)
db.session.add(reservation)
db.session.commit()
