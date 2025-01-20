import numpy as np

'''
def scalar_multiply(matrix, scalar):
    matrix = np.array(matrix)
    return matrix*scalar
'''

def scalar_multiply(matrix, scalar):
    result = []
    for row in matrix:
        temp = []
        for item in row:
            temp.append(item*scalar)
        result.append(temp)
    return result

print(scalar_multiply([[1,2],[2,3]], 3))