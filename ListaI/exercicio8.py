#Faça o contrario do exercicio 7, de Fahrenheit para Celsius.

temp = float(input('Qual a temperatura a ser convertida?(Em Fahrenheit)'))
tempfinal = ((temp-32)*5)/9

print(f'A temperatura convertida para Celsius é de {tempfinal:.1f} graus')