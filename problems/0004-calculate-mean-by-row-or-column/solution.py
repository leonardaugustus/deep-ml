def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:


	if mode == "row":
		result = [0 for x in matrix]
		n = len(matrix[0])
		for i,rows in enumerate(matrix):
			subresult = 0
			for element in rows:
				subresult += element
			result[i] = subresult / n
	
	else:
		result = [0 for x in matrix[1]]
		rows= len(matrix)
		cols = len(matrix[0])

		for i in range(cols):
			for j in range(rows):
				result[i] +=  matrix[j][i] *  1/rows
	return result



