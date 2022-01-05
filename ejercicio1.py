#! usr/bin/env/python
#-*- coding: utf-8 -*-

import sys
import PyQt5.uic as gui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QProcess
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import keyboard

global h, x_vals, y_vals, y_acum, reinicio;
x_vals=[];
y_vals=[];
y_acum=[];
y_ini=0;
h=0;
reinicio=False;
def animate(i,y_ini=0):
	global h, x_vals, y_vals, y_acum, reinicio;
	if keyboard.is_pressed('r') or reinicio==True:
		h=i;
		reinicio=False
	#fin if 
	x_vals.append(i);
	if keyboard.is_pressed('1'):
		y_var=1;
	elif keyboard.is_pressed('2'):
		y_var=2;
	elif keyboard.is_pressed('3'):
		y_var=3;
	elif keyboard.is_pressed('4'):
		y_var=4;
	elif keyboard.is_pressed('5'):
		y_var=5;
	else:
		y_var=0;
	#fin if 
	y_vals.append(y_var);
	y_acum.append(sum(y_vals[h:]));
	x_valsN=(75/1000)*np.array(x_vals);
	if i>=400:
		x_vals.pop(0);
		y_acum.pop(0); 
	#fin if 
	plt.cla(); #Esto al parecer, lo único que hace es "limpiar los ejes"
	plt.plot(x_valsN[-400:],y_acum[-400:]);
#fin función
ani=animation.FuncAnimation(plt.gcf(), lambda x: animate(x), interval=75);

class el_gui1(QMainWindow):
	global reinicio;
	def __init__(self):
		super().__init__();
		gui.loadUi("GUI1.ui",self);
		self.BotonEjecutar.clicked.connect(self.generar_animacion);
		self.BotonReiniciar.clicked.connect(self.fn_reiniciar);
		self.label_2.setText("Bienvenido al ejercicio1");
	#fin inicializacion
	
	def generar_animacion(self):
		plt.tight_layout();
		plt.show();
		self.label_2.setText("La gráfica a continuación");
		self.BotonEjecutar.setEnabled(False);
	#fin funcion 
	
	def fn_reiniciar(self):
		global reinicio;
		reinicio=True;
		self.label_2.setText("He reiniciado!");
	#fin desactivar
	
#fin clase
app=QApplication(sys.argv);
GUI=el_gui1();
GUI.show();
sys.exit(app.exec_());
