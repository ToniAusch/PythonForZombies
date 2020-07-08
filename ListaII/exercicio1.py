#Faça um programa que peça três lados de um triângulo. 
#O programa deverá informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, e o mesmo é: equilátero, isósceles ou escaleno. 

a = int(input('digite o lado A do triângulo: '))
b = int(input('digite o lado B do triângulo: '))
c = int(input('digite o lado C do triângulo: '))

if a+b > c and a+c > b and c+b > a:
    print('É um triângulo')
    if a == b == c: 
        print('O triângulo é Equilátero.')
    elif a == b != c or a == c != b or c == b != a:
        print('O triângulo é Isósceles.')
    else:
        print('O triângulo é Escaleno.')
else:
    print('Não é um triângulo.')

