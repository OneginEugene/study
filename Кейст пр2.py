import random


d = random.randint(1, 100)


def game(n):
    if n == d:
        return 1
    elif n < d:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")
    return 0


attempts = 0
max_attempts = 5

while attempts < max_attempts:
    try:
        n = int(input("Введите загаданное число!: "))
    except ValueError:
        print('Давайте ещё разок, введите целое число.')
        continue

    attempts += 1

    if game(n):
        print("Поздравляем! Вы угадали число.")
        break
    else:
        if attempts < max_attempts:
            print(f"Попробуйте ещё раз. Осталось попыток: {max_attempts - attempts}")
        else:
            print("К сожалению, вы исчерпали все попытки. Игра окончена.")
            print(f"Загаданное число было: {d}")
