import requests
from bs4 import BeautifulSoup


def main():
    url = "https://bank.gov.ua/ua/markets/exchangerates"

    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Помилка при завантаженні сторінки: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')


    table = soup.find('table', id='exchangeRates')

    if not table:
        print("Таблицю з курсами не знайдено на сторінці. Можливо, змінилася структура сайту.")
        return

    rows = table.find('tbody').find_all('tr')

    header = f"| {'Код цифровий':<13} | {'Код літерний':<13} | {'Назва валюти':<35} | {'Офіційний курс':<15} |"
    separator = "-" * len(header)

    print(header)
    print(separator)

    for row in rows:
        cols = row.find_all('td')

        if len(cols) >= 5:
            num_code = cols[0].text.strip()
            char_code = cols[1].text.strip()
            name = cols[3].text.strip()
            rate = cols[4].text.strip()

            print(f"| {num_code:<13} | {char_code:<13} | {name:<35} | {rate:<15} |")


if __name__ == "__main__":
    main()
