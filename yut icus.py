import sys
from forex_python.converter import CurrencyRates
c = CurrencyRates()
from forex_python.converter import CurrencyCodes
n = CurrencyCodes()
print("Welcome to Floyd and Jeremy's money converter!"'''
''')
print('==============================================''''
''')
currency1 = input('What would you like to convert? ')
if len(currency1) !=3:
  print('Sorry this is not a valid number:Exiting Program...')
  sys.exit('')
currency2 = input('What would you like to convert it to? ')
if len(currency2) !=3:
  print('Sorry this is not a valid number:EXITING PROGRAM...')
  sys.exit('')
currency3 = int(input('How much would you like to convert'))
if len(currency3) !=3:
  print('Sorry this is not a valid number:EXITING PROGRAM...')
  sys.exit('')
currency5 = currency2.upper()
currency4 = currency1.upper()

print(n.get_symbol(currency5),c.convert(currency4, currency5, currency3))



