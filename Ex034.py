#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
Salario = float(input('Informe seu salário: '))

if Salario > 1250:
    Calc = Salario + (Salario * 10 / 100)
    print('Novo salário = {}'.format(Calc))
else: 
    Calc2 = Salario + (Salario * 15 / 100)
    print('Novo salário = {}'.format(Calc2))
