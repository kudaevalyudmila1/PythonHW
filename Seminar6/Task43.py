# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

def number_list(x):
    list_1 = []
    for _ in range(x):
        list_1.append(int(input('Введите элемент массива: ')))
    return list_1


def count_pair(list_1: list):
    sum_count = 0
    for i in set(list_1):
        sum_count += list_1.count(i) // 2
    return sum_count


n = int(input('Введите количество элементов  списка:'))
list_1 = number_list(n)
print(list_1)
print(count_pair(list_1))