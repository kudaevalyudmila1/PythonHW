#  Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def grade(a, b): 
        
    if b == 0:
        return 1
    if b ==1:
        return a
    return grade(a, b - 1) * a  

a1 = int(input('Введите число: '))
b1 = int(input('Введите степень: '))
print(grade(a1, b1))