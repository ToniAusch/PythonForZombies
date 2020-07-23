#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
#seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Digite a nota: '))
while nota < 0 or nota > 10: 
    print('Notas somente entre 0 e 10: ')
    nota = float(input('Digite a nota: '))
