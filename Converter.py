import requests

print("Simple Currency Converter")
print("The source is: http://api.fixer.io/latest?base=SGD")
url = 'http://api.fixer.io/latest?base=SGD'
r = requests.get(url)
print("Status code: ", r.status_code)

response_dict = r.json()
print("The base is: ", response_dict['base'])

# dict of stored values for each currency
currencies = response_dict['rates']
print("Currencies returned: ", len(currencies))

while True:	
	currency = input("What is the code of currency you want to convert to? Ex. USD, GBP, INR >> ")
	localcash = float(input("How much SGD do you have? >> "))

	foreigncash = float(currencies.get(currency))
	print("The conversion rate at this time is: ", foreigncash)
	conversion = localcash * foreigncash
	print("You have: %.2f" %conversion, " in ", currency, ".")
	print("--------------------------------------------------------")
