#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
Nome = str(input('Informe seu nome: '))

NomeMa = Nome.upper()
print(NomeMa)

NomeMi = Nome.lower()
print(NomeMi)

print(len(Nome) - Nome.count(' '))

