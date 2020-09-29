def sum(a, b, c):
    return a+b+c
def composition(a, b, c):
    return a*b*c
A = int(input('Введите первое число: '))
B = float(input('Введите второе число: '))
C = int(input('Введите третье число: '))
print('Сумма введенных чисел: ', sum(A, B, C))
print('Произведение введенных чисел', composition(A, B, C))
