import random

def guess_the_number():
    secret_number = random.randint(1, 10)
    attempts = 3

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 10. У вас есть 3 попытки, чтобы угадать его.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Попытка {attempt}: Введите ваше предположение: "))
        except ValueError:
            print("Пожалуйста, введите целое число от 1 до 10.")
            continue

        if guess < 1 or guess > 10:
            print("Число должно быть в диапазоне от 1 до 10.")
            continue

        if guess == secret_number:
            print(f"Поздравляем! Вы угадали число с {attempt}-й попытки.")
            break
        else:
            if attempt < attempts:
                print("Неверно. Попробуйте еще раз.")
            else:
                print(f"Вы проиграли. Загаданное число было: {secret_number}")

if __name__ == "__main__":
    guess_the_number()
