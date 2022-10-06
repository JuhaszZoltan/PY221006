jegy = int(input('milyen jegyet kaptál: '))

if jegy == 1:
    print('az osztályzat: elégtelen')
else:
    if jegy == 2:
        print('az osztályzat elégséges')
    else:
        if jegy == 3:
            print('az osztályzat közepes')
        else:
            if jegy == 4:
                print('az osztályzat: jó')
            else:
                if jegy == 5:
                    print('az osztályzat: jeles')
                else:
                    print('valami nem stimmel...')