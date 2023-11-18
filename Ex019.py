#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

Aluno1 = str(input('Informe o nome do primeiro aluno: '))
Aluno2 = str(input('Informe o nome do segundo aluno '))
Aluno3 = str(input('Informe o nome do tereiro aluno: '))
Aluno4 = str(input('Informe o nome do quarto aluno: '))

lista = [Aluno1, Aluno2, Aluno3, Aluno4]
Escolhido = random.choice(lista) 

print('Escolhido = {}'.format(Escolhido))

