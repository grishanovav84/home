def binary_search(arr, target):
    """Итеративный бинарный поиск.
    Возвращает индекс элемента target в отсортированном списке arr
    или -1, если элемент не найден."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # середина текущего отрезка
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # ищем в правой половине
        else:
            right = mid - 1  # ищем в левой половине

    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """Рекурсивный бинарный поиск."""
    if right is None:
        right = len(arr) - 1

    if left > right:  # отрезок пуст — элемента нет
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


arr = [11, 12, 22, 25, 34, 64, 90]

print(binary_search(arr, 25))            # 3
print(binary_search(arr, 64))            # 5
print(binary_search(arr, 100))           # -1 (не найден)
print(binary_search_recursive(arr, 11))  # 0
print(binary_search_recursive(arr, 90))  # 6
print(binary_search_recursive(arr, 7))   # -1 (не найден)
