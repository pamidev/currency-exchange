from requests import get


def currency_check(currency):
    has_3 = False
    has_alpha = False
    if len(currency) == 3:
        has_3 = True
    for char in currency:
        if char.isalpha():
            has_alpha = True
    if has_3 and has_alpha:
        return True

def data_check(data):
    if len(data) == 10:
        try:
            data_to_check = data.split("-")
            if len(data_to_check[0]) == 4 and len(data_to_check[1]) == 2 and len(data_to_check[2]) == 2:
                return True
            else:
                return False
        except:
            return False
    else:
        False
     

print("Program przelicza kursy walut na złotówki (PLN) wg kursów średnich z Tabeli A NBP.")
currency = input("Podaj walutę w standardzie 3 literownym, np. USD: ")
currency_check(currency)
while currency_check(currency) is not True:
    currency = input("Podaj poprawnie walutę w standardzie 3 literownym, np. USD: ")
currency = currency.upper()

data = input("Podaj datę w formacie YYYY-MM-DD: ")
while data_check(data) is not True:
    data = input("Podaj poprawnie datę w formacie YYYY-MM-DD: ")

resp = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{data}/?format=json")

if resp.ok:
    stream = resp.json()
    ex_rate = stream['rates'][0]['mid']
    print(f"Kurs 1 {currency} = {ex_rate} PLN w dniu {data}")
else:
    print("Brak danych.")
