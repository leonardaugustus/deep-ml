import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	magnitude = 0
	for i in gradient:
		magnitude += i**2
	magnitude = magnitude ** 0.5

	direction = []
	try:
		for i,e in enumerate(gradient):
			direction.append(e / magnitude)
	except ZeroDivisionError:
		direction = [x*0 for x in gradient]
	
	descent_direction = [-x for x in direction]

	# zero edge case:
	if gradient == [x*0 for x in gradient]:
		magnitude = 0

	return {
		"magnitude": magnitude,
		"direction": direction,
		"descent_direction": descent_direction
	}
	

