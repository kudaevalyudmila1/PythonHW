# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

# from random import randint
# size= int(input('Введите размер массива: '))
# list_1 = []
# i = 0
# while i < size:
#     list_1.append(randint(1, 30)) 
#     i += 1  
# print(list_1)
# x = int(input('Введите натуральное число: '))
# i = 0
# min = x - list_1[i]
# while i < size:
#     if abs(x - list_1[i]) <= abs (min):
#         min = x - list_1[i]  
#         b = i 
#     i += 1
# print(f'Наиболее близкое число:{list_1[b]}')

# преподаватель

from random import randint
n = int(input('Введите количество элементов: '))
lst = [randint(1, n) for i in range(n)]
print(lst)
# input_set = {1, 2, 3, 5, 9, 12}
input_set = set(lst)
# num = 11
num = int(input('Введите искомое число: '))
dif = 0
if num > max(input_set):
    print(max(input_set))
elif num < min(input_set):
    print(min(input_set))
else:
    while True:
        if num - dif in input_set and num + dif in input_set and num - dif != num + dif:
            print(num - dif, num + dif)
            break
        elif num - dif in input_set:
            print(num - dif)
            break
        elif num + dif in input_set:
            print(num + dif)
            break
        else:
            dif += 1