# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

from random import randint
size= int(input('Введите размер массива: '))
x = int(input('Введите натуральное число: '))
list_1 = []
i = 0
count = 0
while i < size:
    list_1.append(randint(1, 10)) 
    i += 1  
print(list_1)
c = list_1.count(x)
print(c)