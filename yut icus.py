from forex_python.converter import CurrencyRates
c = CurrencyRates()
from forex_python.converter import CurrencyCodes
n = CurrencyCodes()
print("Welcome to Floyd and Jeremy's money converter!"'''
''')
print('==============================================''''
''')
currency1 = input('What would you like to convert? ')
currency2 = input('What would you like to convert it to? ')
currency3 = int(input('How much would you like to convert'))
print(c.convert(currency1, currency2, currency3),n.get_symbol(currency2))



