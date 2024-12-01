import requests

url = "https://catfact.ninja/fact"
url1 = "https://api.coindesk.com/v1/bpi/currentprice.json"

#task 1

response = requests.get(url)

jason = response.json()
actual = jason[next(iter(jason))]

vowels = "aeiouAEIOU"
count = 0

for letter in actual:
    if letter in vowels:
        count += 1

print(count)

#taks 2

response1 = requests.get(url1)

while True:
    try:
        user_budget = float(input("Enter your budget: "))
        if user_budget > 0:
            break
        else:
            print("Budget must be greater than zero.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

rate = response1.json()['bpi']['USD']['rate']
amount_available = user_budget / float(response1.json()['bpi']['USD']['rate_float'])

print(f"you can afford {amount_available} BTC")


#task 3
name = input("Enter your name: ")
url2 = f"https://api.agify.io/?name={name}"

response2 = requests.get(url2)
data = response2.json()

if data['age'] is not None:
    print(f"the age of Your name is {data['age']} Years!")
else:
    print(f"There's no age of your name.")

