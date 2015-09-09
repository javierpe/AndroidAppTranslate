
/*
 * Copyright (C) 2015 Francisco Javier <http://www.nightwhistler.net>
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
 */

import os
from xml.dom import minidom
import goslate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from DataAccess import DataString

__author__ = 'Estacion1'

class ImportData():


    def deleteAllData(self):
        scriptdir = os.path.dirname(os.path.abspath(__file__))
        sp_file_db = os.path.join(scriptdir, "payroll_db.sqlite")
        engine = create_engine(r'sqlite:///data.sqlite',connect_args={'check_same_thread':True}, poolclass=StaticPool)
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        try:
            for tsr in s.query(DataString).all():
                s.delete(tsr)
            s.commit()
            s.close()
        except Exception as e:
            print e
            s.rollback()
            s.close()


    def importFile(self, window, path, languageTo):
        self.deleteAllData()
        file = open(path)
        gs = goslate.Goslate()
        doc = minidom.parse(file)
        data = doc.getElementsByTagName('string')

        engine = create_engine('sqlite:///data.sqlite',connect_args={'check_same_thread':True}, poolclass=StaticPool)
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()

        for d in range(len(data)):
            window.lbProcess.setText('Processing element %d/%d'%(d, len(data)))
            attr_name = data[d].attributes['name'].value
            text = data[d].firstChild.nodeValue
            translation = gs.translate(text, languageTo)

            print "---------------------------"
            print "Len : ", len(data)
            print "Attribute Name : ", attr_name
            print "Text : ", text
            print "Translated: ", translation
            print "Language to: ", languageTo

            try:

                ins = DataString(name=attr_name,
                            value=text,
                            translation=translation,
                            language_translation=languageTo)
                s.add(ins)
                s.commit()

            except Exception as e:
                window.lbProcess.setText(str(e))
                print e
                s.rollback()

        window.lbProcess.setText('Finished!')
        window.btExportFile.setEnabled(True)