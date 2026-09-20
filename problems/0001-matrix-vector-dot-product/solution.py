import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	a = np.array(a)
	b = np.array(b)

	# check
	result = list()
	if not a.shape[-1] == b.shape[0]:
		return -1
	
	for row in a:
		value = sum([x * y for x,y in zip(row, b)])
		result.append(value)
	return result

	



	



	