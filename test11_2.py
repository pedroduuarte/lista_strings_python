"""QUESTÃO 2:
Faça um programa que permita ao usuário digitar o seu nome e em seguida
mostre o nome do usuário de trás para frente utilizando somente letras
maiúsculas. Dica: lembre-se que ao informar o nome, o usuário pode digitar
letras maiúsculas ou minúsculas.
"""

name = input('Digite aqui o seu nome completo: ',)
print('Seu nome é:' +  name. upper())
i = -1 
print('E seu nome ao contrário é: ', end='')
for i in range (len(name)): 
    print (name[-i-1]. upper(), end='')