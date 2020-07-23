#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
#anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
#crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
#necessários para que a população do país A ultrapasse ou iguale a população do país B,
#mantidas as taxas de crescimento

ano = 0 
a = 80000
b = 200000
while a <= b:
    a = a + a * 0.03
    b = b + b * 0.015
    ano = ano + 1
print(f'Vai demorar {ano} anos para o pais A igualar ou passar a população do pais B')