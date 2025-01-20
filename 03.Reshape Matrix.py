import numpy as np

def reshape_matrix(a, new_shape):
	np_a = np.array(a)
	return np_a.reshape(new_shape)