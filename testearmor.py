import math

x = int(input('Vida: '))
z = int(input('Quantidade de enchants: '))

def calcEnch(i):

    if (z == 0):
        print ('jumento como vai encantar o bagui com 0')
    elif (z < 0):
        print('burro negativo nao da')
    else:
        AumentoI = x * z * i / 100
        novo = x + AumentoI
        novo = math.ceil(novo)

        print (f'AumentoI: {AumentoI}')
        print (f'novo: {novo}')

calcEnch(5)
