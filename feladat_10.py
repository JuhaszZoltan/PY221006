tomeg = int(input('Írd be hány Kg vagy: '))
magassag = int(input('Írd be hány cm magas vagy: ')) / 100

tti = tomeg / (magassag ** 2)
print(f'TTI = {round(tti, 2)}:', end=' ')

if tti < 16: print(f'"súlyos soványság"')
elif tti < 17: print(f'"mérsékelt soványság"')
elif tti < 18.5: print(f'"enyhe soványság"')
elif tti < 25: print(f'"normális testsúly"')
elif tti < 30: print(f'"túlsúlyos"')
elif tti < 35: print(f'"I. fokú elhízás"')
elif tti < 40: print(f'"II. fokú elhízás"')
else: print(f'"III. fokú (súlyos) elhízás"')