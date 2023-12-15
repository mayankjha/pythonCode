import numpy as np
# Declare a dictionary
#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#dict['Age'] = 8; # update existing entry
#dict['School'] = "DPS School"; # Add new entry
#print ("dict['Age']: ", dict['Age'])
#print ("dict['School']: ", dict['School'])

# THis is dictionary
stock_prices = {}
with open ("stockprice.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

print(stock_prices.update({"12-March":"325"}))
print(stock_prices)
