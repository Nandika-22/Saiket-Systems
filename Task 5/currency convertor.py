print("-"*50)
print("         CURRENCY CONVERTER        ")
print("-"*50)
rates = {
    "USD": 1.0,
    "INR": 83.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 148.0
}
amount = float(input("Enter amount: "))
from_currency = input("From currency (USD, INR, EUR, GBP, JPY): ").upper()
to_currency = input("To currency (USD, INR, EUR, GBP, JPY): ").upper()
amount_in_usd = amount / rates[from_currency]
converted_amount = amount_in_usd * rates[to_currency]
print("Converted Amount:", round(converted_amount, 2), to_currency)21
