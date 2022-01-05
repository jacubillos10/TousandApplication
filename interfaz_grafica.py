#! usr/bin/env/python
#-*- coding: utf-8 -*-

import sys
import PyQt5.uic as gui
from PyQt5.QtWidgets import QMainWindow, QApplication

class el_gui1(QMainWindow):
	
	def __init__(self):
		super().__init__();
		gui.loadUi("GUI1.ui",self);
		self.BotonReiniciar.setEnabled(False);
		self.BotonEjecutar.clicked.connect(self.fn_activar);
		self.BotonReiniciar.clicked.connect(self.fn_desactivar);
	#fin inicializacion
	
	def fn_activar(self):
		self.BotonReiniciar.setEnabled(True);
		self.BotonEjecutar.setEnabled(False);
		self.label_2.setText("Activado");
	#fin activar
	
	def fn_desactivar(self):
		self.BotonEjecutar.setEnabled(True);
		self.BotonReiniciar.setEnabled(False);
		self.label_2.setText("DESATIVADO");
	#fin desactivar
	
#fin clase


app=QApplication(sys.argv);
GUI=el_gui1();
GUI.show();
sys.exit(app.exec_());

