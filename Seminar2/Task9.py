# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
number = int(input('Введите натуральное число: '))

if number >= 0:
    result = 1
    n = 1
    while n <= number:
        result = result * n
        n = n + 1
else:
    print('Введено ненатуральное число')
print(f'Факториал числа {number} = {result}')

x = int(input('Введите число: '))


# def factorial(n):
# res = 1
# i = 1
# while i <= n:
# if n > 0:
# res *= i
# i += 1
# if n == 0:
# print(res)
# print(res)


# factorial(x)