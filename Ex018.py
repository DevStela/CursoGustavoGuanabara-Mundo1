#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math 
Angulo = float(input('Informe um angulo: '))

Seno = math.sin(math.radians(Angulo))
print('Seno = {:.2f}'.format(Seno))

Cosseno = math.cos(math.radians(Angulo))
print('Cosseno = {:.2f}'.format(Cosseno))

Tangente = math.tan(math.radians(Angulo))
print('Tangente = {:.2f}'.format(Tangente))
