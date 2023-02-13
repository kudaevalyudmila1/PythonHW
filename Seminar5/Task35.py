# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

def num_is_prim(x):
    if x == 1:
     return 'No'
    for f in range(2, x):
        print(f' {f = }')
        if x % f == 0:
            return 'No'
    return 'Yes' 
        
print (num_is_prim(int(input('Введите натуральное число:'))))