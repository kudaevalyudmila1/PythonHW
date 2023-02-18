# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

from random import randint


def index_interval(min, max, list_1):
    list_2 = []
    for i in range(len(list_1)):
        if  min < list_1[i] < max:
            list_2.append(i)
    return list_2


num_min = int(input('Введите нижнюю границу диапазона:'))
num_max = int(input('Введите верхнюю границу диапазона:'))
n = int(input('Введите количество элементов: '))
lst_1 = [randint(1, 40) for i in range(n)]
print(lst_1)
print(index_interval(num_min, num_max, lst_1))