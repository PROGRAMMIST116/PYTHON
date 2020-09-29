def v_sred(a=5, b=4, c=3):
    return ((a+b+c)/3)
print(v_sred())
x1, x2, x3 = map(int, input('Введите три числа (пробел не забудьте): ').split( ))
v = v_sred(x1, x2, x3)
print(v)
