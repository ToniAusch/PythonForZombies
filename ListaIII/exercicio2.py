#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
#nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input('Digite o nome do usuario: ')
senha = input('Digite a senha: ')
while usuario == senha: 
    print('O nome de usuario e senha não podem ser iguais, insira as informações novamente.')
    usuario = input('Digite o nome do usuario: ')
    senha = input('Digite a senha: ')
print('Informações inseridas com sucesso.')