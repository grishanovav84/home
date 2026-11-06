def find_max(arr):

    if not arr:
        raise ValueError("Массив не должен быть пустым")

    max_value = arr[0]
    for value in arr[1:]:
        if value > max_value:
            max_value = value
    return max_value


if __name__ == "__main__":
    numbers = [3, 7, 1, 9, 4, 2, 8]
    print(f"Массив: {numbers}")
    print(f"Максимальное значение: {find_max(numbers)}")
