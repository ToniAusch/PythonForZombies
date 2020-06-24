#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
#Calcule o total de segundos.

print('Insira os: ')

dias = int(input('dias: '))
horas = int(input('horas: '))
minutos = int(input('minutos: '))
segundos = int(input('sugundos: '))

totalseg = (dias*24*60*60) + (horas*60*60) + (minutos*60) + segundos

print(f'total de segundos é {totalseg}')
