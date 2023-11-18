#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

Aluno1 = str(input('Informe o nome do primeiro aluno: '))
Aluno2 = str(input('Informe o nome do segundo aluno '))
Aluno3 = str(input('Informe o nome do tereiro aluno: '))
Aluno4 = str(input('Informe o nome do quarto aluno: '))

lista = [Aluno1, Aluno2, Aluno3, Aluno4]
shuffle(lista)
print(lista)