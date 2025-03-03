from typing import List, Union

def give_bmi(height: List[Union[int, float]], weight: List[Union[int, float]]) -> List[float]:
	"""
	Calculate BMI (Body Mass Index)
	Formula: BMI = weight / (height^2)
	"""
	if len(height) != len(weight)
		raise ValueError("Error: height and weight lists must have the same length.")

	if not all(isinstance(h, (int, float)) and isinstance(w, (int, float)) for h, w in zip(height, weight)):
		raise ValueError("Error: All elements in height and weight lists must be integers or floats")

	return [w / (h ** 2) for h, w in zip(height, weight)]

def apply_limit(bmi: List[Union ])

if __name__ == "__main__":
	height = [2.71, 1.15]
	weight = [165.3, 38.4]

	try:
		bmi = get_bmi(height, weight)
		print(f"BMI List: {bmi} (Type: {type(bmi)})")
		print(f"Above Limit (26): {apply_limit(bmi,26)}")

	except ValueError as e:
		print(e)
