# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum1(a, b):
    if b == 0:
        return a
    return sum1(a, b - 1) + 1

a1 = int(input('Введите первое число: '))
b1 = int(input('Введите второе число: '))
if b1 > a1:
    a1, b1 = b1, a1
print(sum1(a1, b1))