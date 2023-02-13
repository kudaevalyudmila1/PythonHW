# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint
n = int(input('Введите количество элементов первого набора чисел: '))
m = int(input('Введите количество элементов второго набора чисел: '))
lst_1 = [randint(1, 10) for i in range(n)]
lst_2 = [randint(1, 10) for i in range(m)]
print(lst_1, lst_2)
lst_1, lst_2 = set(lst_1), set(lst_2)
lst_3 = sorted(lst_1.intersection(lst_2))
print(lst_3)