#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
#preço a pagar.

preço = int(input('Digite o preço original da mercadoria: '))
pordesconto = float(input('Digite o desconto: '))

desconto = preço * pordesconto
valordesconto = preço - desconto

print (f'O valor do desconto é {desconto}')
print (f'O valor do produto com desconto fica {valordesconto}')


