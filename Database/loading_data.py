import pandas as pd
import numpy as np
import os
import pickle

df_variants_train = pd.read_csv('training_variants', usecols=['Gene', 'Variation', 'Class'])
print (df_variants_train.head())

"""
Code for converting the file into csv
"""
# df_variants_train.to_csv('train_data.csv')


"""
Code for creating unique gene sequence 
"""
# def unique_gene(df):

# 	genes_Set = set()
# 	for i in df['Gene']:
# 		genes_Set.add(i)
	
# 	return genes_Set



# gene_Set = unique_gene(df_variants_train)

# for i in gene_Set:
# 	print (i)

# print ("Saving Unique Gene Sequence")
# with open('gene_Set.pkl', 'wb') as f:
# 	pickle.dump(gene_Set, f)

print ("Loading Unique gene sequence")


gene_Set = pickle.load( open( "gene_Set.pkl", "rb" ) )

print (len(gene_Set))

with open( 'protien_seq' + '.pkl', 'wb') as f:
	pickle.dump(protien_seq, f, pickle.HIGHEST_PROTOCOL)
