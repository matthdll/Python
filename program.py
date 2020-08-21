baseados = int(input('Baseados Dia '))
anos = int(input('Anos fumados '))
tempo_para_fumar_um_brau = int(input('Minutos q c demora pra marola: '))
total_baseados = anos * 365 * baseados
dias = total_baseados / ((24 * 60) / tempo_para_fumar_um_brau)
print (f'Vc perdeu {dias:.1f} dias')
