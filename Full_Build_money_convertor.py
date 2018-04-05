#import statements
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)
from forex_python.converter import CurrencyRates
c = CurrencyRates()
from forex_python.converter import CurrencyCodes
n = CurrencyCodes()
class QuietError(Exception):
    pass
#The opening menu
print("Welcome to Floyd and Jeremy's money converter!"'''
''')
print('==============================================''''
''')

#Input statement
while True:
    try:
        option1 = int(input("If you would like to convert an amount of money to another currency please enter the number 1 "
        '''       If you would like to the conversion rates for all the currencies please enter the number 2 ''' + '''
        '''))
        break
    except ValueError:
        print("")
        sys.stdout.write('Please Enter 1 or 2')
        print ('''
        ''')

#If for user error
if option1 is 2: 
  base_rate = input('Please choose a base currency for the conversion rates')
  pp.pprint(c.get_rates(base_rate))
  sys.exit('')
if option1 is 1:
  pass
#input statements 
while True:
    try:
        currency1 = input('What currency would you like to convert? ')
        currency2 = input('What currency would you like to convert it to? ')
        currency3 = int(input('How money much would you like to convert'))
        break
    except ValueError:
        print('')
        sys.stdout.write('Please Enter a valid input. Please do not use decimals')
        print('''
        ''')
#changes currency to uppercase
currency5 = currency2.upper()
currency4 = currency1.upper()
#print all the currencies
print(n.get_symbol(currency5),c.convert(currency4, currency5, currency3))
