# from typing import List


def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints the shape of the original 2D array and the shape after slicing.
    Returns a truncated version of the list based on the start end arguments.

    Args:
        family (list[list[float]]): A 2D list representing height-weight pairs.
        start (int): Start index for slicing.
        end (int): End index for slicing.

    Returns:
        list[list[float]]: The sliced 2D list.

    Raises:
        ValueError: If input is not a 2D list or contains non-numeric values.
    """

    if not isinstance(family, list) or \
            not all(isinstance(row, list) for row in family):
        raise ValueError("Error: Input must be a 2D list.")

    if not all(
        all(isinstance(x, (int, float)) for x in row) for row in family
    ):
        raise ValueError("Error: All elementsmust be numerical.")
    # for row in family:
    #     for x in row:
    #         if not isinstance(x, (int, float)):

    row_len = len(family[0])
    if not all(len(row) == row_len for row in family):
        raise ValueError("Error: All rows should be same size.")

    print(f"My shape is: ({len(family)}, {row_len})")

    sliced_family = family[start:end]

    print(
        f"My new shape is: ({len(sliced_family)}, "
        f"{len(sliced_family[0]) if sliced_family else None})")

    return sliced_family


if __name__ == "__main__":
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print(slice_me(family, 0, 0))
    print(slice_me(family, 1, -2))

    family_bad = [
        [1.80, 78.4],
        [2.15, 102.7, 85.6],  # ⚠️Error!
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    try:
        print(slice_me(family_bad, 0, 2))
    except ValueError as e:
        print(e)
