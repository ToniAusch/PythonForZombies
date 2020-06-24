#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
#esperada para a viagem.

distancia = int(input('Qual distância que vai ser percorrida? (Km)'))
velocidade = int(input('Qual a velocidade média do veiculo? (Km/h) '))

tempo = distancia / velocidade

print(f'O tempo que vai levar para percorrer essa distância nessa velocidade é de {tempo:.2f} horas')

