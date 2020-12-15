from config import *

from controllers.user_controller import *
from controllers.audience_controller import *
from controllers.reservation_controller import *
db.create_all()


if __name__ == '__main__':
    app.run()