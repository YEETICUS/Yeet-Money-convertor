#import statements
import sys
from forex_python.converter import CurrencyRates
c = CurrencyRates()
from forex_python.converter import CurrencyCodes
n = CurrencyCodes()
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
        sys.stdout.write('Invalid Input EXITING PROGRAM...')

#If for user error
if option1 is 2: 
  base_rate = input('Please choose a base currency for the conversion rates')
if len(base_rate) == 3:
  print(c.get_rates(base_rate))
if len(base_rate) !=3:
  sys.exit('Invalid input. EXITING PROGRAM...')
  sys.exit('')
if option1 is 1:
  pass

#If input is invalid exit program
else:
  print('Invalid Input')
  sys.exit('EXITING PROGRAM...')
  
#input statements 
currency1 = input('What currency would you like to convert? ')

#If the input is not in the format of a currency exit program
if len(currency1) !=3:
  print('Sorry this is not a valid number. EXITING PROGRAM...')
  sys.exit('')
currency2 = input('What currency would you like to convert it to? ')
if len(currency2) !=3:
  print('Sorry this is not a valid number. EXITING PROGRAM...')
  sys.exit('')
currency3 = int(input('How money much would you like to convert'))
if currency3 < 0:
  print('Sorry this is not a valid number. EXITING PROGRAM...')
  sys.exit('')


#changes currency to uppercase
currency5 = currency2.upper()
currency4 = currency1.upper()
#print all the currencies
print(n.get_symbol(currency5),c.convert(currency4, currency5, currency3))
