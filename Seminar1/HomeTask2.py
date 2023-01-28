# Найдите сумму цифр трехзначного числа. 

number = int(input('Введите число: '))
print(number)
if  99 < number < 1000:
    res = number // 100 + number // 10 % 10 + number % 10
else:
    res = ('введено не трехзначное число')
print(res)