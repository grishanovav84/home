def linear_search(arr, target):
    """Итеративный линейный поиск.
    Возвращает индекс первого вхождения элемента target в список arr
    или -1, если элемент не найден."""
    for i in range(len(arr)):
        if arr[i] == target:  # сравниваем каждый элемент с искомым
            return i

    return -1


def linear_search_all(arr, target):
    """Линейный поиск всех вхождений элемента.
    Возвращает список индексов, по которым встречается target
    (пустой список, если элемент не найден)."""
    result = []
    for i in range(len(arr)):
        if arr[i] == target:
            result.append(i)

    return result


def linear_search_recursive(arr, target, i=0):
    """Рекурсивный линейный поиск.
    Возвращает индекс элемента target в списке arr
    или -1, если элемент не найден."""
    if i >= len(arr):  # дошли до конца — элемента нет
        return -1

    if arr[i] == target:
        return i

    return linear_search_recursive(arr, target, i + 1)


arr = [4, 7, 2, 9, 7, 5, 1]

print(linear_search(arr, 9))              # 3
print(linear_search(arr, 1))              # 6
print(linear_search(arr, 100))            # -1 (не найден)
print(linear_search_all(arr, 7))          # [1, 4] (два вхождения)
print(linear_search_all(arr, 100))        # [] (не найден)
print(linear_search_recursive(arr, 2))    # 2
print(linear_search_recursive(arr, 5))    # 5
print(linear_search_recursive(arr, 42))   # -1 (не найден)
