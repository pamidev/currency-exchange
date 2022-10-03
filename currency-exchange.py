from requests import get
from datetime import datetime


def currency_validator(entered_currency: str):
    currencies_list = ["THB", "USD", "AUD", "HKD", "CAD", "NZD", "SGD", "EUR", "HUF",
                       "CHF", "GBP", "UAH", "JPY", "CZK", "DKK", "ISK", "NOK", "SEK",
                       "HRK", "RON", "BGN", "TRY", "ILS", "CLP", "PHP", "MXN", "ZAR",
                       "BRL", "MYR", "IDR", "INR", "KRW", "CNY", "XDR"]
    entered_currency = entered_currency.upper()
    for cur in range(len(currencies_list)):
        if entered_currency == currencies_list[cur]:
            return True


def date_validator(entered_date):
    try:
        datetime.strptime(entered_date, '%Y-%m-%d')
        if entered_date >= "2002-01-02":
            return True
        else:
            print("Data nie może być sprzed 2002-01-02.")
            return False
    except ValueError:
        print("Niewłaściwy format daty.")
        return False
     

print("Program przelicza kursy walut na złotówki (PLN) wg kursów średnich z Tabeli A NBP.")
currency = input("Podaj trzyliterowy kod waluty (standard ISO 4217), np. USD, EUR, GBP: ")
currency_validator(currency)
while currency_validator(currency) is not True:
    currency = input("Podaj poprawnie trzyliterowy kod waluty (standard ISO 4217), np. USD, EUR, GBP: ")
currency = currency.upper()

date = input("Podaj datę w formacie RRRR-MM-DD (standard ISO 8601): ")
while date_validator(date) is not True:
    date = input("Niewłaściwa data.\nPodaj poprawną datę w formacie RRRR-MM-DD (standard ISO 8601): ")

resp = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/?format=json")

if resp.ok:
    stream = resp.json()
    try:
        currency_des = stream['currency']
        ex_rate = stream['rates'][0]['mid']
        print(f"Kurs waluty: 1 {currency} ({currency_des}) wynosi {ex_rate} PLN w dniu {date}")
    except KeyError:
        print("Brak danych o kursie dla wybranej waluty w podanym dniu.")
else:
    print("Brak połączenia z bazą danych NBP.")
