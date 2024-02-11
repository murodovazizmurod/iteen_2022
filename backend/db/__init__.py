from ormx import Database
from ormx.models import Table, Column

# ORMX - my own framework


db = Database('data.db')


# Table model
class Device(Table):
    __tablename__ = 'devices'
    model = Column(str)
    cost = Column(float)
    income = Column(float)

    def __repr__(self):
        return f"{self.model}"


# creating structure
db.create(Device)