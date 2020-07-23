#A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
#formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
#soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
#de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

n = int(input('Digite um número inteiro: '))

a,b = 1,1
cont = 1

while cont <= n-2:
    a, b = b, a + b
    cont = cont + 1

print(f'O número de Fibonacci é {b}.')