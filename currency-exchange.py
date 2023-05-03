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
    print("Too many arguments entered. Try again.")
    sys.exit(1)
elif two_currency:
    print("You are trying to enter two arguments, which are probably currency code. Try again.")
    sys.exit(1)
elif short_currency_code:
    print("Incorrect length of currency code. Check it and try again.")
    sys.exit(1)

try:
    for argument in arguments:
        good_currency = argument.upper() in CURRENCIES
        bad_currency = len(argument) == 3 and argument.upper() not in CURRENCIES
        if good_currency:
            currency = argument.upper()
            arguments.remove(argument)
        if bad_currency:
            print("No data available for this currency. Try with a different currency.")
            sys.exit(1)
except IndexError:
    currency = ""

print("This Python program converts currency exchange rates into Polish zlotys (PLN) "
      "according to the average exchange rates from Table A of the National Bank of Poland on the given day.")

while currency not in CURRENCIES:
    currency = input("Enter three-letter currency code according to the ISO 4217 standard: ").upper()

try:
    date = arguments[0]
except IndexError:
    date = input("Enter date: ")
try:
    date_to_format = parser.parse(date)
    date = datetime.strftime(date_to_format, '%Y-%m-%d')
except ValueError:
    print("The date is not entered correctly. Check it and try again.")
    sys.exit(1)

response = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/?format=json")

if response.status_code == 200:
    stream = response.json()
    currency_name = stream['currency']
    exchange_rate = stream['rates'][0]['mid']
    print(f"Currency exchange rate {currency_name} on {date} is: 1 {currency} = {exchange_rate} PLN")
elif response.status_code == 400:
    print("Incorrect data has been entered. Check it and try again.")
elif response.status_code == 404:
    print("No data available for this currency on the day.")
elif response.status_code == 500:
    print("Server error of the National Bank of Poland.")
else:
    print("Connection to API of the National Bank of Poland is not currently available.")
    print("The reason is unknown.")
