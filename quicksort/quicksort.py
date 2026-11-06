def quicksort(arr, low=0, high=None):
    """Быстрая сортировка (Quicksort).

    Выбираем опорный элемент (pivot), разделяем список на две части:
    слева — элементы меньше pivot, справа — больше, и рекурсивно
    сортируем обе части. Сортировка выполняется на месте (in-place).

    Сложность:
        Время:  O(n log n) в среднем, O(n^2) в худшем случае
        Память: O(log n) — стек рекурсии
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Разделяем список и получаем индекс опорного элемента
        pivot_index = partition(arr, low, high)

        # Рекурсивно сортируем части слева и справа от pivot
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

    return arr


def partition(arr, low, high):
    """Схема Ломуто: ставит pivot на своё место и возвращает его индекс."""
    pivot = arr[high]   # последний элемент — опорный
    i = low - 1         # граница элементов, меньших pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Ставим pivot на своё финальное место
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6, 7]
    print("Исходный список: ", data)
    quicksort(data)
    print("Отсортированный: ", data)
