'''
# using the unpack operator * and zip() function
def transpose_matrix(a):
	b = zip(*a)
	result = [list(i) for i in b]
	
	return result
'''

'''
# from scratch 
def transpose_matrix(a):
	transpose = []
	row = len(a)
	col = len(a[0])
	
	for i in range(col):
		result = []
		for j in range(row):
			result.append(a[j][i])
		transpose.append(result)
	return transpose
'''

import numpy as np

def transpose_matrix(a):
	return np.transpose(a)


r = transpose_matrix([[1,2,3],[4,5,6]])
print(r)