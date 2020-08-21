velocidade = int(input('Velocidade do carro: '))
if velocidade > 110:
    print ('Voce foi multado fdp')
    multa = (velocidade - 110) * 5
    print (f'Voce ta devendo {multa:.2f}')
else:
    print ('Siga em frente!')