#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário. 

salarioinicial = int(input('Digite seu salario atual: '))
aumento = float(input('Digite a porcentagem do aumento: '))

valoraumentado = salarioinicial * aumento  

salariofinal = salarioinicial + valoraumentado 

print(f'O valor do aumento é de R$ {valoraumentado}')
print(f'O salario com aumento será de R${salariofinal}')