import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	dot = np.dot(v1, v2)
	b_left = (np.sum(v1**2))**0.5
	b_right = (np.sum(v2**2))**0.5
	
	return dot / (b_left * b_right)


v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
print(round(cosine_similarity(v1, v2), 3))
