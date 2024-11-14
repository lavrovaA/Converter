import requests


def get_exchange_rate():

    response = requests.get('https://v6.exchangerate-api.com/v6/6017d6ae294fb326dedc903a/latest/USD')


    if response.status_code == 200:
        return response.json()['conversion_rates']['RUB']
    else:
        print("Ошибка при получении курса. Проверьте наличие подключения к интернету.")
        return None


def convert_rubles_to_dollars(rubles, exchange_rate):
    return rubles / exchange_rate


def main():
    print("КОНВЕРТЕР ВАЛЮТ (Рубли <-> Доллары)")

    exchange_rate = get_exchange_rate()

    if not exchange_rate:
        return

    print(f"Актуальный курс: 1 USD = {exchange_rate:.2f} RUB")

    while True:
        try:
            rubles = float(input("Введите сумму в рублях (или '0' для выхода): "))

            if rubles == 0:
                print("Выход из программы.")
                break

            dollars = convert_rubles_to_dollars(rubles, exchange_rate)
            print(f"{rubles:.2f} RUB = {dollars:.2f} USD")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите числовое значение.")


if __name__ == '__main__':
    main()

