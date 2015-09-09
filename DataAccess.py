# -*- coding: utf-8 -*-
import sys
from Settings import Settings
reload(sys)
sys.setdefaultencoding("utf-8")
__author__ = 'Estacion1'

from numbers import Real

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
Base = declarative_base()

class DataString(Base):
    __tablename__ = 'data_string'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    translation = Column(String)
    language_translation = Column(String)

    def __repr__(self):
        return str(self.id) + "#"\
               + str(self.name)\
               + "#" + str(self.value) \
               + "#" + str(self.translation)\
               + "#" + str(self.language_translation)

c = Settings()
if c.validatePath('data.sqlite') is False:
    print("Creando base de datos")
    engine = create_engine('sqlite:///data.sqlite',connect_args={'check_same_thread':False}, poolclass=StaticPool)

    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
else:
    print("La base de datos ya esta creada")