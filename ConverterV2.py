import requests
import re

print("Simple Currency Converter v2")
print('ELECTRIC BOOGALOO')
print("The source is: http://api.fixer.io/latest")
print('=========================================')


while True:
	print("\nPlease input your commands in this fashion:")
	print("'convert' <amount> <currency> 'to' <currency>")
	print("Ex: convert 100 sgd to myr")
	userRequest = input('\nEnter your command: ')

	commandList = userRequest.split(' ')

	while len(commandList) != 5 and commandList[0] != 'convert' and commandList[3] != 'to':
		print("Not quite right, do it exactly like this: ")
		print("'Convert' <amount> <currency> 'into' <currency>")
		userRequest = input('Enter your command: ')

	base_currency = commandList[2].upper()
	currency = commandList[4].upper()
	localcash = commandList[1]


	url = 'http://api.fixer.io/latest?base=' + base_currency
	r = requests.get(url)
	print("\nStatus code: ", r.status_code)
	# dict of stored values for each currency
	response_dict = r.json()
	currencies = response_dict['rates']
	print("Currencies returned: ", len(currencies))

	foreigncash = currencies.get(currency)
	print("--------------------------------------------------------")
	print("The conversion rate at this time is: ", foreigncash)
	conversion = int(localcash) * foreigncash
	print("You have: %.2f" %conversion, " in ", currency, ".")
	print("--------------------------------------------------------")
