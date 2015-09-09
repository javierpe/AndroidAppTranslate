# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AAT.ui'
#
# Created: Wed Sep 09 12:06:25 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

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
import threading
import warnings

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import goslate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from Export import ExportData

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 273)
        MainWindow.setFixedSize(500, 273)
        MainWindow.setStyleSheet(_fromUtf8("QWidget#centralwidget{background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(186, 186, 186, 255), stop:0.781095 rgba(235, 235, 235, 255));}\n"
"\n"
"QToolButton, QToolButton:pressed{\n"
"\n"
"background-color:transparent;\n"
"border:none;\n"
"color: rgb(156, 156, 156);\n"
"\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed{\n"
"\n"
"background-color:rgb(219,218,206);\n"
"border: 1px solid  rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"\n"
"background-color:rgb(89,209,171);\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked:hover{\n"
"\n"
"background-color:rgb(219,218,206);\n"
"\n"
"}\n"
"\n"
" QPushButton {\n"
"font: 75 14pt \"Segoe UI Light\";\n"
"    background-color: rgb(0, 150, 136);\n"
"    color: rgb(255, 255, 255);\n"
"     border-width: 2px;\n"
"     border-radius: 10px;\n"
"    border-color: rgb(0, 150, 136);\n"
"     font: bold 16px;\n"
"     min-width: 10em;\n"
"     padding: 6px;\n"
" }\n"
" QPushButton:pressed {\n"
"    background-color: rgb(77,182, 172);\n"
" }\n"
"\n"
"QLineEdit {\n"
"\n"
"    border-style: solid;\n"
"    border: 2px solid gray;\n"
"    border-radius: 8px;\n"
"    \n"
"    color: rgb(159, 159, 159);\n"
"     font: 75 14pt \"Segoe UI Light\";\n"
"     border-width: 2px;\n"
"     border-radius: 10px;\n"
"     min-width: 10em;\n"
"     padding: 6px;\n"
"\n"
" }\n"
"\n"
"QLabel{\n"
"font: 63 15pt \"Segoe UI Light\";\n"
"color: rgb(156, 156, 156);\n"
"}\n"
"\n"
"QGroupBox{\n"
"color: rgb(156, 156, 156);\n"
"}\n"
"\n"
"QProgressBar {\n"
"     border: 2px solid grey;\n"
"     border-radius: 5px;\n"
"    text-align: center;\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: #05B8CC;\n"
"background-color: rgb(0, 150, 136);\n"
"     width: 20px;\n"
" }\n"
"QCheckBox{\n"
"font: 63 15pt \"Segoe UI Light\";\n"
"color: rgb(0, 150, 136);\n"
"}\n"
"\n"
"\n"
"/* QComboBox STYLE */\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 5em;\n"
"    height: 30px;\n"
"    font: 63 15pt \"Segoe UI Light\";\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btImportRes = QtGui.QPushButton(self.centralwidget)
        self.btImportRes.setGeometry(QtCore.QRect(260, 120, 222, 51))
        self.btImportRes.setStyleSheet(_fromUtf8(" QPushButton:pressed {\n"
"    background-color: rgb(0,151, 167);\n"
" }\n"
" QPushButton{\n"
"background-color: rgb(1, 87, 155);\n"
"}\n"
""))
        self.btImportRes.setObjectName(_fromUtf8("btImportRes"))
        self.lbTo = QtGui.QLabel(self.centralwidget)
        self.lbTo.setGeometry(QtCore.QRect(30, 130, 131, 21))
        self.lbTo.setObjectName(_fromUtf8("lbTo"))
        self.btExportFile = QtGui.QPushButton(self.centralwidget)
        self.btExportFile.setGeometry(QtCore.QRect(260, 190, 222, 51))
        self.btExportFile.setStyleSheet(_fromUtf8("\n"
" QPushButton:pressed {\n"
"    background-color: rgb(0,150, 136);\n"
" }\n"
" QPushButton{\n"
"background-color: rgb(0, 191, 165);\n"
"}\n"
"\n"
""))
        self.btExportFile.setObjectName(_fromUtf8("btExportFile"))
        self.lbProcess = QtGui.QLabel(self.centralwidget)
        self.lbProcess.setGeometry(QtCore.QRect(10, 10, 481, 91))
        self.lbProcess.setStyleSheet(_fromUtf8(" border: 2px solid  #B2DFDB;"))
        self.lbProcess.setTextFormat(QtCore.Qt.AutoText)
        self.lbProcess.setAlignment(QtCore.Qt.AlignCenter)
        self.lbProcess.setWordWrap(True)
        self.lbProcess.setObjectName(_fromUtf8("lbProcess"))
        self.comboTo = QtGui.QComboBox(self.centralwidget)
        self.comboTo.setGeometry(QtCore.QRect(20, 160, 221, 51))
        self.comboTo.setObjectName(_fromUtf8("comboTo"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Android App Translate", None))
        self.btImportRes.setText(_translate("MainWindow", "Import string resource", None))
        self.lbTo.setText(_translate("MainWindow", "Translate to", None))
        self.btExportFile.setText(_translate("MainWindow", "Export", None))
        self.lbProcess.setText(_translate("MainWindow", "Android Application Translate", None))



        #QtCore.QObject.connect(self.comboFrom, QtCore.SIGNAL("currentIndexChanged(int)"), self.onItemFromSelected)
        QtCore.QObject.connect(self.comboTo, QtCore.SIGNAL("currentIndexChanged(int)"), self.onItemToSelected)

        QtCore.QObject.connect(self.btExportFile, QtCore.SIGNAL("clicked()"), self.exportFile)
        QtCore.QObject.connect(self.btImportRes, QtCore.SIGNAL("clicked()"), self.selectResourceString)

    dataLanguages = {}
    fromKey = ""
    toKey = ""


    def onItemToSelected(self, item):
        self.toKey = ""
        selectedLanguage = self.comboTo.currentText()
        self.toKey = self.dataLanguages[str(selectedLanguage)]

    def onItemFromSelected(self, item):
        self.fromKey = ""
        selectedLanguage = self.comboFrom.currentText()
        self.fromKey = self.dataLanguages[str(selectedLanguage)]

    def selectResourceString(self):
        in_path = QtGui.QFileDialog.getOpenFileName(self, u'Select string.xml resource', '')
        fileName, fileExtension = os.path.splitext(str(in_path))

        if fileExtension != '':
            if str(fileExtension) != '.xml':
                QtGui.QMessageBox.critical(self, u'System', u' Wrong file, the file should contain the XML extension.',QtGui.QMessageBox.Ok)
            else:
                self.lbProcess.setText(in_path)
                self.btExportFile.setEnabled(False)
                e = ImportData()
                t = threading.Thread(target=e.importFile, args=(self, in_path, self.toKey), name='ServiceImport')
                t.start()

    def exportFile(self):
        self.importEvo = True
        engine = create_engine('sqlite:///data.sqlite',connect_args={'check_same_thread':True}, poolclass=StaticPool)
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        language = ""
        try:

            ln = s.query(DataAccess.DataString.language_translation).first()
            language =  ln[0]
            if language == '':
                language = self.toKey

        except Exception as e:
            language = self.toKey


        fileName = QFileDialog.getSaveFileName(self, 'Save as','strings-%s'%(language), selectedFilter='*.xml')
        if fileName:
            e = ExportData()
            t = threading.Thread(target=e.exportToXMLFileString, args=(self, fileName, self.toKey), name='ServiceExportToXML')
            t.start()




    def loadLanguage(self):

        gs = goslate.Goslate()
        print gs.get_languages()
        data = gs.get_languages()
        count = 0
        for string in data:
            key = json.dumps(string)
            key = key.split('"')
            key = key[1]
            language =  gs.get_languages()[key]
            self.dataLanguages[language] = key
            #print count, language
            #self.comboFrom.setItemText(count, _translate("MainWindow", key, None))
            #self.comboFrom.addItem(_fromUtf8(language))

            #self.comboTo.setItemText(count, _translate("MainWindow", key, None))
            self.comboTo.addItem(_fromUtf8(language))

            count += 1



import json
import DataAccess
from Import import ImportData
from xml.dom import minidom
import wx

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    sits = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(sits)
    ui.loadLanguage()
    sits.show()
    sys.exit(app.exec_())

