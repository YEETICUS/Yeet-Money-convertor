from forex_python.converter import CurrencyRates
c = CurrencyRates()
currency1 = input('What would you like to convert? ')
currency2 = input('What would you like to convert it to? ')
y = c.convert(currency1, currency2, 1)
print(y)
