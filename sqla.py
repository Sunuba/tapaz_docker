#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import datetime


Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(191), nullable=False)
    price = Column(String(150), nullable=False)
    valyuta = Column(String(50), nullable=False)
    code = Column(String(191), nullable=False)
    tarix = Column(DateTime, default=datetime.datetime.utcnow)


engine = sqlalchemy.create_engine('mysql+pymysql://tapaz:password@mysql/tapaz')
Base.metadata.create_all(engine)
