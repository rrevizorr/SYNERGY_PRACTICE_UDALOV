def sum_negatives_between_min_max(arr):
    if not arr:
        return 0
    
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))
    
    start = min(min_index, max_index)
    end = max(min_index, max_index)
    
    sum_neg = 0
    for num in arr[start + 1 : end]:
        if num < 0:
            sum_neg += num
    
    return sum_neg

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число!")

def input_array():
    n = input_int("Введите размер массива: ")
    while n <= 0:
        print("Размер массива должен быть положительным!")
        n = input_int("Введите размер массива: ")
    
    arr = []
    print("Введите элементы массива (по одному в строке):")
    for i in range(n):
        while True:
            try:
                num = int(input(f"Элемент {i + 1}: "))
                arr.append(num)
                break
            except ValueError:
                print("Ошибка: введите целое число!")
    return arr


print("Программа вычисляет сумму отрицательных элементов между min и max")
arr = input_array()
result = sum_negatives_between_min_max(arr)
print("Сумма отрицательных элементов между минимальным и максимальным:", result)