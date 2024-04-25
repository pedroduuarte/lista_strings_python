"""
QUESTÃO 14:
Faça um programa em que troque todas as ocorrencias de uma letra L1 pela
letra L2 e da L2 pela L1 em uma string. A string e as letras L1 e L2 devem ser
fornecidas pelo usuario. Obs: Não utilize a função replace().
"""

str = input('Digite um texto qualquer: ')
L1 = input('Digite a letra L1: ')
L2 = input('Digite a letra L2: ')
str2 = ''
for x in str:
    if x == L1: 
        x = L2
    elif x == L2: 
        x = L1
    str2 += x
print(str2)
