#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Nome = str(input('Informe seu nome: ')).upper().strip().split()

print('Primeiro nome = {}'.format(Nome[0]))
print('Ultimo nome = {}'.format(Nome[len(Nome)-1]))
