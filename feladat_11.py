arlista = '''
======árlista======
alma      599 Ft/Kg
körte     899 Ft/Kg
szilva   1099 Ft/Kg
===================
'''
print(arlista)

folytatas = True
vegosszeg = 0

while folytatas:
    ar = 0
    termek = input('mit szeretnél vásárolni? ')
    if termek == 'alma': ar = 599
    elif termek == 'körte': ar = 899
    elif termek == 'szilva': ar = 1099
    else: print('nincs ilyen termék!')
    mennyiseg = float(input(f'Mennyi {termek}t szeretnél vásárolni (Kg)? '))
    vegosszeg += ar * mennyiseg
    if input('szeretnél még valamit vásárolni? ') != 'igen':
        folytatas = False
print(f'Összesen {round(vegosszeg)} Ft lesz!')
print('viszont látásra!')