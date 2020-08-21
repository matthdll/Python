import math

s = float(input('Dano inicial da arma: '))
x = float(input('Dano final da arma: '))
z = float(input('Quantidade de enchants%: '))

AumentoI = s * z * (5 / 100)
AumentoF = x * z * (5 / 100)
novo = s + AumentoI
novo2 = x + AumentoF
novo = math.ceil (novo)
novo2 = math.ceil (novo2)

print (f'AumentoI: {AumentoI}')
print (f'AumentoF: {AumentoF}')
print (f'Novo dano Inicial: {novo}')
print (f'Novo dano final: {novo2}')
