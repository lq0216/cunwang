# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker

from model import engine, Boke


class DbBoke():
    def __init__(self):
        self.db_session = self.getDBSession()

    def getDBSession(self):
        Session = sessionmaker(bind=engine)
        return Session()

    def add(self, obj):
        self.db_session.add(obj)
        self.db_session.commit()

    def delete(self, title):
        self.db_session.query(Boke).filter(Boke.title == title).delete()
        self.db_session.commit()

    def update(self, obj):
        self.db_session.query(Boke).filter(Boke.title == obj.title).update({obj.title: obj.text})
        self.db_session.commit()

    def get(self, title):
        ret = self.db_session.query(Boke).filter_by(title=title).all()
        self.db_session.commit()
        return ret

    def getAll(self):
        ret = self.db_session.query(Boke).all()
        self.db_session.commit()
        return ret
