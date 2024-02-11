from ormx import Database
from ormx.models import Table, Column


db = Database('data.db')


class Device(Table):
    __tablename__ = 'devices'
    model = Column(str)
    cost = Column(float)
    income = Column(float)

    def __repr__(self):
        return f"{self.model}"


db.create(Device)


for d in open('init_db/data.txt', 'rb').readlines():
    d = d.decode("utf-8").strip().split(',')
    a = Device(model=d[0], cost=float(d[1]), income=float(d[2]))
    db.save(a)
