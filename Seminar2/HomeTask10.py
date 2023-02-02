# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import randint
quantity_coins = int(input('Введите количество монет: '))
print(f'{quantity_coins} ->',end=' ')
count_0, count_1 = 0, 0
for i in range(quantity_coins):
    temp = randint(0, 1)
    print(temp, end=' ')
    if temp == 0:
        count_0 += 1
    else:
       count_1 += 1 

print()    
if count_0 > count_1:
    print(count_1)
elif count_0 < count_1:
     print(count_0)
else:
    print(f'Количество монет "орёл" и "решка" одинаковое {count_0}, переворачивайте любые')
