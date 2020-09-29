def days(k):
    return k%7 + 1
try:
    K = int(input('Введите номер от 1 до 365: '))
    if K > 365 or K < 1:
        raise ValueError()
    else: print('Номер дня недели (1 — понедельник, 2 — вторник, ..., 6 — суббота, 7 — воскресенье): ', days(K))
except ValueError:
    print('Вы ввели неверное число!')
