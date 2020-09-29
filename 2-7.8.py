import random
print('Первый игрок')
a = random.randint(1, 6)
print(a)
print('Второй игрок')
b = random.randint(1, 6)
print(b)
if a > b:
    print('Победил первый игрок')
else:
    print('Победил второй игрок')
