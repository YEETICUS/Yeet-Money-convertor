from fixerio import Fixerio
import pandas
import json
currency1 = input("What do you want to convert from? ")
currency2 = input("What do you want to convert to? ")
fxrio = Fixerio(base= currency1)
fxrio = Fixerio(symbols=[currency1, currency2])
fxrio.latest(symbols=[currency1, currency2])
print("Currency amount here for the first currency you inputted " + currency1 + " is worth " + " Currency 2 amount here " + currency2 )
input(fxrio.latest())
