#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
CatetoO = float(input('Informe o cateto oposto: '))
CatetoA = float(input('Informe o Cateto adjecente: '))

Hipotenusa = (CatetoO ** 2) + (CatetoA ** 2)

print('Hipotenusa = {}'.format(Hipotenusa))
