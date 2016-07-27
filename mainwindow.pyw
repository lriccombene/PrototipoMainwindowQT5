#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QDialog
from PyQt5 import uic
from form_profesionales import Ui_form_profesionales

class Mainwindow(QMainWindow):
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        uic.loadUi("mainwindow.ui", self)
        self.actionAgregar_Profesional.triggered.connect(self.Agregar_Profesional)

    def Agregar_Profesional(self):
        #from pdb4qt import set_trace; set_trace()
        self.form_profesionales=QDialog()
        self.ui=Ui_form_profesionales()
        self.ui.setupUi(self.form_profesionales)
        self.form_profesionales.show()

app = QApplication(sys.argv)
_ventana = Mainwindow()
_ventana.show()
app.exec_()
