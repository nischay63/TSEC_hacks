import pandas as pd
import pickle
import os

import numpy as np
import re


def newProtien(str):
	return str[-1]

def findpos(str):
	tempf = re.match(r'[A-Z][0-9]+[A-Z]', str)
	if tempf is None:
		return -1
	else:
		return int(str[1:-1])

df =  pd.read_csv('training_variants', usecols=['Gene', 'Variation', 'Class'])
protien_base_gene = pickle.load( open( "nnngene_sequence_Set.pkl", "rb" ))

database = pd.DataFrame(columns = ['Gene Sequence','Class'])

freq_table = dict()
counter = 0

for index,row in df.iterrows():
	if row['Gene'] not in protien_base_gene.keys():
		continue
	if row['Gene'] in freq_table.keys():
		if(freq_table[row['Gene']] > 100):
			continue
		else:
			freq_table[row['Gene']]+=1
	else:
		freq_table[row['Gene']] = 1

	try:
		gene_sequence = protien_base_gene[row['Gene']]
		pos = findpos(row['Variation'])-1
		if pos == -1:
			continue
		gene_sequence = gene_sequence[:pos] + str(newProtien(row['Variation']))
		if "addkeyvaluetoadictinpython" in gene_sequence:
			print (gene_sequence[:pos], row['Variation'])
		database.loc[counter] = [gene_sequence,row['Class']]
		counter+=1
		print (counter)
	except:
		continue

print (database.head(10))
database.to_csv('new_database.csv')


