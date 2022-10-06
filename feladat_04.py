euro_arfolyama = float(input('Mennyi az € árfolyama jelenleg? '))
huf = int(input('Mennyi HUF-ot szeretnél átváltani? '))
print(f'A nálad lévő {huf}Ft {round(huf / euro_arfolyama, 2)}€-t ér.')