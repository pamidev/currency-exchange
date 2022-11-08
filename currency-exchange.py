import sys
from requests import get
from dateutil import parser
from datetime import datetime

CURRENCIES = ("THB", "USD", "AUD", "HKD", "CAD", "NZD", "SGD", "EUR", "HUF",
              "CHF", "GBP", "UAH", "JPY", "CZK", "DKK", "ISK", "NOK", "SEK",
              "HRK", "RON", "BGN", "TRY", "ILS", "CLP", "PHP", "MXN", "ZAR",
              "BRL", "MYR", "IDR", "INR", "KRW", "CNY", "XDR")

arguments = sys.argv[1:]
to_many_args = len(arguments) > 2
two_currency = len(arguments) == 2 and len(arguments[0]) == len(arguments[1]) == 3
short_currency_code = len(arguments[0]) < 3 or len(arguments[1]) < 3

currency = ""
date = ""

if to_many_args:
    print("Wprowadzono za dużo argumentów. Spróbuj ponownie.")
    sys.exit(1)
elif two_currency:
    print("Próbujesz wprowadzić dwa argumenty, które są prawdopodobnie kodami walut. Spróbuj ponownie.")
    sys.exit(1)
elif short_currency_code:
    print("Nieprawidłowa długość kodu waluty. Sprawdź ją i spróbuj ponownie.")
    sys.exit(1)

try:
    for argument in arguments:
        good_currency = argument.upper() in CURRENCIES
        bad_currency = len(argument) == 3 and argument.upper() not in CURRENCIES
        if good_currency:
            currency = argument.upper()
            arguments.remove(argument)
        if bad_currency:
            print("Brak danych dla wprowadzonej waluty. Spróbuj wprowadzić inny kod waluty.")
            sys.exit(1)
except IndexError:
    currency = ""

print("Program przelicza kursy walut na złotówki (PLN) wg kursów średnich z Tabeli A NBP z podanego dnia.")

while currency not in CURRENCIES:
    currency = input("Wprowadź trzyliterowy kod waluty wg standardu ISO 4217: ").upper()

try:
    date = arguments[0]
except IndexError:
    date = input("Podaj datę: ")
try:
    date_to_format = parser.parse(date)
    date = datetime.strftime(date_to_format, '%Y-%m-%d')
except ValueError:
    print("Wprowadzono nieprawidłowo datę. Sprawdź ją i spróbuj ponownie.")
    sys.exit(1)

response = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/?format=json")

if response.status_code == 200:
    stream = response.json()
    currency_name = stream['currency']
    exchange_rate = stream['rates'][0]['mid']
    print(f"Kurs waluty {currency_name} w dniu {date} wynosi: 1 {currency} = {exchange_rate} PLN")
elif response.status_code == 400:
    print("Wprowadzono nieprawidłowe dane. Sprawdź je i spróbuj ponownie.")
elif response.status_code == 404:
    print("Brak danych o kursie wybranej waluty w podanym dniu.")
elif response.status_code == 500:
    print("Błąd serwera Narodowego Banku Polskiego.")
else:
    print("Brak połączenia z API Narodowego Banku Polskiego.")
