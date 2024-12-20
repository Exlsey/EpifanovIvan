def calculator():
    print("Добро пожаловать в консольный калькулятор!")
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    while True:
        choice = input("Введите номер операции (1/2/3/4) или 'q' для выхода: ")

        if choice == 'q':
            print("Выход из калькулятора.")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка ввода. Пожалуйста, вводите числа.")
                continue

            if choice == '1':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Деление на ноль недопустимо.")
                else:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Некорректный выбор операции. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    calculator()

