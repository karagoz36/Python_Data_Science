from typing import List, Union


def give_bmi(height: list[float], weight: list[float]) -> list[float]:
    """
    Calculate BMI (Body Mass Index) for given height and weight lists.
    Formula: BMI = weight / (height^2)

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[float]: List of BMI values.
    """
    if len(height) != len(weight):
        raise ValueError("Error: height and weight are not same length.")

    if not all(
        isinstance(h, (int, float)) and isinstance(w, (int, float))
        for h, w in zip(height, weight)
    ):
        raise ValueError("Error: All elements must be integers or floats")

    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: List[Union[int, float]], limit: int) -> List[bool]:
    """
    Apply a threshold to BMI values.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): The threshold value.

    Returns:
        list[bool]: List where True means the BMI is above the limit.

    Raises:
        ValueError: If BMI list contains non-numeric values.
    """
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("Error: Only numeric values.")

    return [b > limit for b in bmi]


if __name__ == "__main__":
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    try:
        bmi = give_bmi(height, weight)
        print(f"BMI List: {bmi} (Type: {type(bmi)})")
        print(f"Above Limit (26): {apply_limit(bmi,26)}")

    except ValueError as e:
        print(e)
