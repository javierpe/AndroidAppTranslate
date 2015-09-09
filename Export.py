from xml.dom import minidom
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from DataAccess import DataString

__author__ = 'Estacion1'

import xml.etree.cElementTree as ET

class ExportData():

    def exportToXMLFileString(self, window, path, languageTo):
        window.lbProcess.setText('Writing file...')
        p = str(path).split('strings')
        newPath = p[0] + 'values-%s/'%(languageTo) + 'string.xml'

        try:
            engine = create_engine('sqlite:///data.sqlite',connect_args={'check_same_thread':True}, poolclass=StaticPool)
            session = sessionmaker()
            session.configure(bind=engine)
            s = session()


            data = s.query(DataString.name, DataString.value, DataString.translation).all()
            if len(data) != 0:

                root = ET.Element("resources")

                for string in data:
                    ET.SubElement(root, "string", name=string[0]).text = string[2]


                tree = ET.ElementTree(root)
                tree.write(path)

                xmlstr = minidom.parseString(ET.tostring(tree.getroot(), 'utf-8')).toprettyxml(indent="    ")
                with open(path, "w") as f:
                    f.write(xmlstr)

                window.lbProcess.setText('Process finished! Please rename the file.')
                window.btExportFile.setEnabled(True)
            else:
                window.btImportRes.setEnabled(True)
                window.lbProcess.setText('Empty Database. Please import an XML file')
        except Exception as e2:
            window.lbProcess.setText('Error creating XML file!')
            window.btExportFile.setEnabled(False)

