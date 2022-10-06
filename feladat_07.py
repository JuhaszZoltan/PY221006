from math import sqrt, pow

a = int(input('egyik befogó hossza (cm): '))
b = int(input('másik befogó hossza (cm): '))
if a > 0 and b > 0:
    print(f'Átfogó hossza: {(a ** 2 + b ** 2) ** .5} cm')
    print(f'Átfogó hossza: {sqrt(pow(a, 2) + pow(b, 2))} cm')
else:
    print(f'Nincs olyan derlékszögű háromszög, aminek a befogói {a} és {b}')