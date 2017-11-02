# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker

from model import engine, Boke, Users


class DB():
    def __init__(self):
        self.db_session = self.getDBSession()

    def getDBSession(self):
        Session = sessionmaker(bind=engine)
        return Session()

    def add(self, obj):
        self.db_session.add(obj)
        self.db_session.commit()

    # boke
    def deleteBoke(self, title):
        self.db_session.query(Boke).filter(Boke.title == title).delete()
        self.db_session.commit()

    def updateBoke(self, title, text):
        self.db_session.query(Boke).filter(Boke.title == title).update({title: text})
        self.db_session.commit()

    def getBoke(self, title):
        ret = self.db_session.query(Boke).filter_by(title=title).all()
        self.db_session.commit()
        return ret

    def getAllBoke(self):
        ret = self.db_session.query(Boke).all()
        self.db_session.commit()
        return ret

    # users
    def deleteUser(self, name):
        self.db_session.query(Users).filter(Users.name == name).delete()
        self.db_session.commit()

    def updateUserPasswd(self, name, passwd):
        self.db_session.query(Users).filter(Users.name == name).update({name: passwd})
        self.db_session.commit()

    def getUsers(self, name):
        ret = self.db_session.query(Users).filter_by(name=name).all()
        self.db_session.commit()
        return ret
