# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/lqtest?charset=utf8", max_overflow=5, encoding="utf-8")

Base = declarative_base()

# 创建单表
class Users(Base):
   __tablename__ = 'users'
   id = Column(Integer, primary_key=True, autoincrement=True)
   name = Column(String(32))
   extra = Column(String(16))

class Boke(Base):
   __tablename__ = 'boke'
   id = Column(Integer, primary_key=True, autoincrement=True)
   title = Column(String(100), primary_key=True)
   text = Column(String(1000), default='red')

Base.metadata.create_all(engine)  #创建表
# Base.metadata.drop_all(engine)   #删除表
