# import tensorflow as tf
# import keras
from sklearn.preprocessing import LabelEncoder	
import pandas as pd
import numpy as np
"""
Deep Learning Model Libraries
"""
# from keras.utils import to_categorical
# from keras.models import Sequential
# from keras.layers import LSTM, Dense, TimeDistributed


def preprocess(database):

	X = np.zeros((database.shape[0],2000,27))
	print (X.shape)
	y = []
	counter = 0
	for index, row in database.iterrows():
		gene_seq = row['Gene Sequence']
		prop = []
		for i in gene_seq:
			if ord(i) - 65 > 26:
				print ("Error Solved")
				continue

			prop.append(ord(i) - 65)

		for i in range(len(prop)):
			X[counter][i][prop[i]] = 1

		counter+=1
		print (counter)
	# 	t = [0]*len(prop)
	# 	x = [t]*27
	# 	print (len(x[0]))
	# 	for i in range(len(prop)):
	# 		x[prop[i]][i] = 1
		
	# 	# print ("Appending to X")
	# 	X.append(x)
	# 	print ("X shape : ",len(X),", ",len(X[0]))
			
		

		yy = [0,0,0,0,0,0,0,0,0]
		yy[row['Class']-1] = 1
		y.append(yy)
	# 	print ("Y Shape : ",np.array(y).shape)
			
		

	print("Shape : ",np.array(X).shape , np.array(y).shape)
	print ("Saving the data")
	kk = 0
	newX = []
	for i in range(X.shape[0]):
		newXX = []
		for j in range(len(X[i])):
			if np.sum(X[i][j]) == 0:
				break
			else:
				newXX.append(X[i][j])
		newX.append(newXX)

	print ("New Dataset  :", len(newX),len(newX[0]),len(newX[0][0]))

	np.save('X_data',X)
	np.save('y_data',y)
	return np.array(X) , np.array(y)

# def dl_model(shape):	

# 	model = Sequential()
# 	model.add(LSTM(32, return_sequences=True, input_shape=(None, 26)))
# 	model.add(Activation('relu'))
# 	model.add(LSTM(8))
# 	model.add(Activation('relu'))
# 	#model.add(TimeDistributed(Dense(2, activation='relu')))
# 	model.add(Dense(16,activation = 'relu'))
# 	model.add(Dense(9,activation = 'softmax'))
# 	print(model.summary())

# 	model.compile(loss='categorical_crossentropy',
# 	          optimizer='adam')


database = pd.read_csv('new_database.csv')
preprocess(database)

