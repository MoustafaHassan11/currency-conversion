import requests

API_KEY = "3Bml6YwwLGdVk1ZZcd7VeTq8NRywyTJ0"
API_URL = "https://api.apilayer.com/fixer/convert"

def get_user_input():
    while True:
        try:
            to = input("Enter the initial currency: ").upper()
            from_currency = input("Enter the target currency: ").upper()
            amount = float(input("Enter the currency amount: "))
            if amount <= 0:
                print("Amount must be greater than 0")
                continue
            else:
                return to, from_currency, amount
        except ValueError:
            print("Invalid entry. The amount must be a numeric value.")

def make_api_request(to, from_currency, amount):
    url_params = {
        "to": from_currency,
        "from": to,
        "amount": amount
    }

    headers = {"apikey": API_KEY}

    try:
        response = requests.get(API_URL, headers=headers, params=url_params)
        response.raise_for_status()  # Raise an HTTPError for 4xx/5xx status codes
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def main():
    to, from_currency, amount = get_user_input()
    result = make_api_request(to, from_currency, amount)

    if result:
        print(result)
    else:
        print("Error. Please try again later.")

if __name__ == "__main__":
    main()

