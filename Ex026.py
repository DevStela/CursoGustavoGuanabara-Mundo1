#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
Frase = str(input('Informe uma frase: ')).upper().strip
print('Letra A aparece {} vezes'.format(Frase.count('A')))
print('Aparece a primeira vez na posição {}'.format(Frase.find('A')+1))
print('Aparece a ultima vez na posição {}'.format(Frase.rfind('A')+1))