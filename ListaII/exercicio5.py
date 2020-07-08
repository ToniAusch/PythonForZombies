#Faça um programa que leia três números e mostre o maior e o menos deles

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a>b and a>c: 
    print(f'O primeiro número ({a}) é o maior.')

elif b>a and b>c:
    print(f'O segundo número ({b}) é o maior.')

elif c>a and c>b:
    print(f'O terceiro número ({c}) é o maior.')
    
else: 
    print('Tem números iguais nessa comparação')

if a<b and a<c:
    print(f'O primeiro número ({a}) é o menor.')
elif b<a and a<c:
    print(f'O segundo número ({b}) é o menor.')
elif c<a and c<b: 
    print(f'O segundo número ({c}) é o menor.')