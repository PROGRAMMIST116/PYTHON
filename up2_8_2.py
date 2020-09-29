def upperifsn(s, n):
    """Возвращает строку в верхнем регистре если длина строки s больше n"""
    if len(s) > n:
        return s.upper()
    else:
        return s

if __name__ == "__main__":
    str_new = str(input('Введите строку: '))
    other_n = int(input('Введите число n: '))
    print(upperifsn(str_new, other_n))