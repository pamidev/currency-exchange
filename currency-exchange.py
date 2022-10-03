from requests import get
from datetime import datetime


def currency_check(currency):  # walidator walut do poprawy
    has_3 = False
    has_alpha = False
    if len(currency) == 3:
        has_3 = True
    for char in currency:
        if char.isalpha():
            has_alpha = True
    if has_3 and has_alpha:
        return True

def date_validator(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        if date >= "2002-01-02":
            return True
        else:
            print("Data nie może być sprzed 2002-01-02.")
            return False
    except ValueError:
        print("Niewłaściwy format daty.")
        return False
     

print("Program przelicza kursy walut na złotówki (PLN) wg kursów średnich z Tabeli A NBP.")
currency = input("Podaj walutę w standardzie 3 literownym, np. USD: ")
currency_check(currency)
while currency_check(currency) is not True:
    currency = input("Podaj poprawnie walutę w standardzie 3 literownym, np. USD: ")
currency = currency.upper()

date = input("Podaj datę w formacie RRRR-MM-DD: ")
while date_validator(date) is not True:
    data = input("Podaj poprawną datę w formacie RRRR-MM-DD: ")

resp = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/?format=json")

if resp.ok:
    stream = resp.json()
    ex_rate = stream['rates'][0]['mid']
    print(f"Kurs 1 {currency} = {ex_rate} PLN w dniu {date}")
else:
    print("Brak danych.")
