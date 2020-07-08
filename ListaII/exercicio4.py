#Faça um programa que leia três números e mostre o maior deles.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a>b and a>c: 
    print('O primeiro número é o maior.')

elif b>a and b>c:
    print('O segundo número é o maior.')

elif c>a and c>b:
    print('O terceiro número é o maior.')
    
else: 
    print('Tem números iguais nessa comparação')