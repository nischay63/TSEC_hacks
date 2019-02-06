import os
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def anaLyze_Gene():
	gene_Set = pickle.load(open( "gene_Set.pkl", "rb" ))
	df_variants_train = pd.read_csv('training_variants', usecols=['Gene', 'Variation', 'Class'])

	gene_freq = dict()
	for i in df_variants_train['Gene']:
		if i in gene_freq.keys():
			gene_freq[i]+=1
		else:
			gene_freq[i] = 1;

	temp = gene_freq

	print ("Sorting the Frequency")
	gene_freq = sorted(gene_freq,key=gene_freq.__getitem__,reverse = True)

	tp = pd.DataFrame(columns = ['Gene'])
	print ("Sorted Frequency Table")
	y = []
	for i in range(len(gene_freq)):
		y.append(temp[gene_freq[i]])

	y = y[:10]
	

	keys_name = tp['Gene'][:10]
	x = np.array([1,2,3,4,5,6,7,8,9,10])
	my_xticks = [gene_freq[i] for i in range(10)]

	plt.xticks(x,my_xticks)
	plt.bar(x,y)
	plt.show()

def analyzeClass():
	df_variants_train = pd.read_csv('training_variants', usecols=['Gene', 'Variation', 'Class'])

	class_Freq = dict()
	for i in df_variants_train['Class']:
		if i in class_Freq.keys():
			class_Freq[i]+=1
		else:
			class_Freq[i] = 1;

	temp = class_Freq

	print ("Sorting based on class Frequency")
	class_Freq = sorted(class_Freq,key=class_Freq.__getitem__,reverse = True)

	x = [int(q) for q in temp.keys()]
	plt.bar(x,temp.values())
	plt.show()

def analyzeClass_v_Gene():
	gene_Set = pickle.load(open( "gene_Set.pkl", "rb" ))
	df_variants_train = pd.read_csv('training_variants', usecols=['Gene', 'Variation', 'Class'])

	print (df_variants_train.groupby(['Gene','Class']).count())

analyzeClass_v_Gene()
