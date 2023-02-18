# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.


def arithmetic_progression(n, a1, d):
    list_1 = []
    list_1.append(a1)
    for i in range(1, n):
        list_1.append(a1 + i * d)
    return list_1


num = int(input('Введите количество элементов  прогрессии:'))
a_1 = int(input('Введите первый  элемент  прогрессии:'))
step = int(input('Введите разность между соседними элементами  прогрессии:'))
print(arithmetic_progression(num, a_1, step))