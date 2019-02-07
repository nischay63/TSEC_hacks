import os
import tensorflow as tf
from PyQt5 import QtCore, uic, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys

from keras.layers import Bidirectional, Activation
from keras.models import Sequential

import keras

from keras.layers import LSTM, Dropout, Dense
from keras.models import load_model
import numpy as np
print ("Loading Model")
model = load_model('Model9.h5')
print ("Model Loaded")


UIClass, QtBaseClass = uic.loadUiType("tsec.ui")

class MyApp(UIClass, QtBaseClass):


	def __init__(self):
		UIClass.__init__(self)
		QtBaseClass.__init__(self)
		self.setupUi(self)
		self.show()
		k = self.buttonBox.clicked.connect(self.on_click)
		self.show()


	def preprocess(self,gene_seq):

		prop = []
		for i in gene_seq:
			if ord(i)-65>26:
				print ("Error Solved")
				continue
			prop.append(ord(i) - 65)

		X = np.zeros((1,2000,27))
		for i in range(len(prop)):
			X[0][i][prop[i]] = 1
		return X

	def on_click(self):
		textboxValue = self.textEdit.toPlainText()
		oneencoded = self.preprocess(textboxValue)

		y = model.predict(oneencoded)
		y = np.argmax(y[0])
		y+=1
		QMessageBox.question(self , "Message" ,"Predicted class  " + str(y) , QMessageBox.Ok | QtWidgets.QMessageBox.Ok)#, QMessageBox.Ok)
		self.textEdit.setText("")
		self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
