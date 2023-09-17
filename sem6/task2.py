# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

def find_indices_in_range(random_list, min_range, max_range):
    indices = [i for i, x in enumerate(random_list) if min_range <= x <= max_range]
    return indices

n = int(input("Введите количество элементов в списке: "))
min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))

random_list = [random.randint(min_value, max_value) for _ in range(n)]
print("Сгенерированный список:", random_list)

min_range = int(input("Введите минимальное значение диапазона: "))
max_range = int(input("Введите максимальное значение диапазона: "))

indices = find_indices_in_range(random_list, min_range, max_range)
print("Индексы элементов, попадающих в заданный диапазон:")
print(indices)
