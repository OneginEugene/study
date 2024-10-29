import math
import sys

sys.setrecursionlimit(2000)

while True:
    try:
        n =int(input("Введите натуральное целое число!:"))
        break
    except ValueError:
        print('Давайте ещё разок,')
        continue
print('Спасибо!')


def factorial(n):
    if n == 0:
        return 1
    elif n<1:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(n)
print("Факториал числа", n, "равен", result)
