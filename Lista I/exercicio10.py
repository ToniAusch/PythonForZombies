#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#stotal de dias.

#144 cigarros fumados são 1440 minutos perdidos, ou seja, 24 horas. 

fumados = int(input('Quantos cigarros você fuma por dia?'))
anos = int(input('Faz quantos anos que você fuma?'))

totalcigarros = anos * 365 * fumados
diasperdidos = totalcigarros / 144

print(f'Você perdeu {diasperdidos:.1f} dias de vida com essa quantidade de cigarros fumados ')