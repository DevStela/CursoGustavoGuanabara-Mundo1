#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
Computador = randint (0,5)
Usuario = int(input('Estou pensando em um número de 0 a 5. Qual você acha que é? '))

if Computador == Usuario:
    print('Deu empate!')
else: 
    print('Você perdeu!')


