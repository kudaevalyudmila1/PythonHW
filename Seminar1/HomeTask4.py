# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

sum = int(input('Введите общее число журавликов: '))
if sum % 6 == 0:
    x = int(sum / 6)
    z = (x + x) * 2
    print('{} -> {}, {}, {}'.format(sum, x, z, x))
else:
    print('Введено неверное число')