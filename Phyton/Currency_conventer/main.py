import requests
from datetime import datetime

def get_current_rate():
    try:
        # Получаем курс через API
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        data = response.json()
        return data['Valute']['USD']['Value']
    except:
        # В случае ошибки используем фиксированный курс
        return 90.0  # Примерный курс доллара


def convert_currency():
    print("=== Конвертер валют RUB ⟷ USD ===")
    print(f"Текущая дата: {datetime.now().strftime('%d.%m.%Y')}")

    # Получаем текущий курс
    rate = get_current_rate()
    print(f"Текущий курс: 1 USD = {rate:.2f} RUB")

    while True:
        print("\nВыберите операцию:")
        print("1. RUB → USD")
        print("2. USD → RUB")
        print("3. Выход")

        choice = input("Ваш выбор (1-3): ")

        if choice == '3':
            print("Программа завершена. До свидания!")
            break

        if choice not in ['1', '2']:
            print("Неверный выбор. Попробуйте снова.")
            continue

        try:
            if choice == '1':
                amount = float(input("Введите сумму в рублях: "))
                result = amount / rate
                print(f"{amount:.2f} RUB = {result:.2f} USD")
            else:
                amount = float(input("Введите сумму в долларах: "))
                result = amount * rate
                print(f"{amount:.2f} USD = {result:.2f} RUB")

        except ValueError:
            print("Ошибка: Введите корректное числовое значение.")


if __name__ == "__main__":
    convert_currency()