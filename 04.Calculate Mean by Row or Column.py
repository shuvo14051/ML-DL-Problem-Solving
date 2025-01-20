import numpy as np


def calculate_matrix_mean(matrix, mode):
	if mode == 'column':
	    return np.mean(matrix,axis=0)	
	return np.mean(matrix,axis=1)


r = calculate_matrix_mean(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'row')
print(r)

