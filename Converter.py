import requests

print("Simple Currency Converter")
print("The source is: http://api.fixer.io/latest\n")
base_currency = input("\nWhat is your base currency? Ex. HKD, EUR >> ")
url = 'http://api.fixer.io/latest?base=' + base_currency
r = requests.get(url)
print("Status code: ", r.status_code)

response_dict = r.json()
print("The base is: ", response_dict['base'])

# dict of stored values for each currency
currencies = response_dict['rates']
print("Currencies returned: ", len(currencies))

while True:	
	currency = input("\nWhat is the code of currency you want to convert to? Ex. USD, GBP, INR >> ")
	localcash = float(input("How much " + str(base_currency) + " do you have? >> "))

	foreigncash = float(currencies.get(currency))
	print("\nThe conversion rate at this time is: ", foreigncash)
	conversion = localcash * foreigncash
	print("You have: %.2f" %conversion, " in ", currency, ".")
	
