#Determine se um ano é bissexto. Verifique no google como fazer isso. 

import calendar

ano = int(input('Digite o ano: '))
calendar.isleap(ano)

if calendar.isleap(ano) == True: 
    print('O ano é bissexto')
else: 
    print('Não é um ano bissexto')
