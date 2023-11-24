import requests

to = input("Enter the initial currency: ")
from_currency = input("Enter the target currency: ")

while True:
    try:
        amount = float(input("Enter the currency amount: "))
        if amount <= 0:
            print("Amount must be greater than 0")
            continue
        else:
            break
    except ValueError:
        print("Invalid entry. The amount must be a numeric value.")
        continue

url = f"https://api.apilayer.com/fixer/convert?to={from_currency}&from={to}&amount={amount}"

payload = {}
headers = {
    "apikey": "3Bml6YwwLGdVk1ZZcd7VeTq8NRywyTJ0"
}

response = requests.get(url, headers=headers, data=payload)

status_code = response.status_code
if status_code != 200:
    print("Error. Please try again later.")
    quit()

result = response.text
print(result)

