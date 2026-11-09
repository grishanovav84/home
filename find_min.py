"""Utility functions for finding minimum values in arrays/lists."""


def find_min(arr):
    """Return the minimum value in a non-empty array/list.

    Args:
        arr (list): A non-empty list of comparable elements (e.g., numbers).

    Returns:
        The smallest element in ``arr``.

    Raises:
        ValueError: If ``arr`` is empty.
        TypeError: If elements in ``arr`` are not mutually comparable.

    Examples:
        >>> find_min([3, 1, 4, 1, 5, 9])
        1
        >>> find_min([-2, -5, 0, 3])
        -5
        >>> find_min([42])
        42
    """
    if not arr:
        raise ValueError("Cannot find the minimum of an empty array.")

    min_value = arr[0]
    for value in arr[1:]:
        if value < min_value:
            min_value = value
    return min_value


if __name__ == "__main__":
    # Simple demonstration when run directly
    test_cases = [
        [3, 1, 4, 1, 5, 9],
        [-2, -5, 0, 3],
        [42],
        [7, 7, 7, 7],
        [10, 20, 5, 30],
    ]
    for case in test_cases:
        print(f"find_min({case}) = {find_min(case)}")