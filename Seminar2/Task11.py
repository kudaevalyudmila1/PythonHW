# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

number = int(input('Введите натуральное число: '))
n1 = 0
n2 = 1
n_num = 2
while n2 < number:
    n1, n2 = n2, n1 + n2
    n_num = n_num + 1
if  n2 == number:
    print (f'{number}  является числом Фибоначчи {n_num}')
else:
    print (f'{number}  не является числом Фибоначчи')

# user_input = int(input('Введите целое положительное число: '))
# n1, n2 = 0, 1
# n_num = 2
# while n2 < user_input:
#     n1, n2 = n2, n1 + n2
#     n_num += 1
# if n2 == user_input:
#     print(f'{user_input} - число Фиббоначи №{n_num}')
# else:
#     print(f'{user_input} не является числом Фиббоначи')