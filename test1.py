baseados = int(input('Baseados Dia '))
anos = int(input('Anos fumados '))
total_baseados = anos * 365 * baseados
dias = total_baseados / 144
print (f'Vc perdeu {dias:.1f} dias')
