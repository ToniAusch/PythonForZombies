#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
#e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
#quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
#descontos e o salário líquido, conforme a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

earn = int(input('Quanto você recebe por hora?'))
hour = int(input('Quantas hora você trabalhou no último mês?'))

bruto = earn * hour
ir = bruto * 11/100
inss = bruto * 8/100
sin = bruto * 5/100
liquido = bruto - (ir + inss + sin)

print('\n')
print(f'Salário bruto = R${bruto}')
print(f'Imposto de renda = R${ir}')
print(f'Inss = R${inss}')
print(f'Sindicato = R${sin}')
print(f'Salário liquido = R${liquido}')
