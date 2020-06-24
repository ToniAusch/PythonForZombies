#Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

temp = float(input('Qual temperatura a ser convertida?(Em Celsius)'))

tempfinal = ((9*temp)/5)+32

print(f'A temperatura convertida para Fahrenheit é de {tempfinal:.1f} graus')