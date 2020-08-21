n = float(input('Digite sua nota: '))
if (n >= 6 and n <= 10):
    print ('Voce foi aprovado! ')
            
if (n <= 5):
    print ('Voce foi reprovado! ')   

while n < 0 or n > 10:
    n = float(input('Notas apenas de 0 a 10: '))

    if (n >= 6):
        print ('Voce foi aprovado! ')
    if (n <= 5):
        print ('Voce foi reprovado! ')    













