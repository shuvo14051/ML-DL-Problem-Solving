# row = len(matrix)
# col = len(matrix[0])

def matrix_dot_vector(a, b):
	# row_length = len(a)
	col_length = len(a[0])
	result = []
	vector_length = len(b)
	  
	if col_length!=vector_length:
		return -1
	
	for row in a:
		row_sum = 0
		for i in range(len(row)):
			row_sum += row[i] * b[i]
		result.append(row_sum)
		
	return result

	
print(matrix_dot_vector(a = [[1,2],[2,4]], b = [1,2]))
	

