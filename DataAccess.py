# -*- coding: utf-8 -*-

'''
 * Copyright (C) 2015 Francisco Javier <https://mx.linkedin.com/in/fcojavierpena>
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''
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