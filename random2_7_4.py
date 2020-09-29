import random
def start():
    """Игра, угадай число"""
    rand_m = random.randint(1, 5)
    n = int(input('Введите целое число от 1 до 5: '))
    if n != rand_m:
        print('Попробуйте еще раз')
    else:
        print('Вы выйграли!')

if __name__ == "__main__":
    start()