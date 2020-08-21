import math

s = int(input('Dano inicial da arma: '))
x = int(input('Dano final da arma: '))
z = int(input('Quantidade de enchants%: '))

def calcEnch(dano_inicial, dano_final, quantidade_enchant):
    
    if (z == 0):
        print('seu animal com 0 enchant n muda porra nenhuma')
    elif (z < 0):
        print('retardado como que vai enchant negativo')
    else:
        AumentoI = dano_inicial * quantidade_enchant * 5 / 100
        AumentoF = dano_final * quantidade_enchant * 5 / 100
        novo = dano_inicial + AumentoI
        novo2 = dano_final + AumentoF
        novo = math.ceil(novo)
        novo2 = math.ceil(novo2)
        
        print (f'AumentoI: {AumentoI}')
        print (f'AumentoF: {AumentoF}')
        print (f'Novo dano Inicial: {novo}')
        print (f'Novo dano final: {novo2}')
        
calcEnch(s, x, z)







    

