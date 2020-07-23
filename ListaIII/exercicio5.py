#Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
#o algoritmo de Euclides. 

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

while a%b != 0:
    a, b = b, a%b

print(f'O máximo divisor comundo de a e b é {b}.')