def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	scaled = matrix.copy()
	for i,row in enumerate(matrix):
		for j, value in enumerate(row):
			scaled[i][j] = value * scalar
	return scaled

print(scalar_multiply([[1,2],[3,4]], 2))