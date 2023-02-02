# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
num = int(input('Введите число: '))
print(f'{num} ->', end=' ')
num1 = 1
count = 1
while num1 <= num:
   print(num1, end=' ')
   num1 = 2 ** count
   count+= 1 