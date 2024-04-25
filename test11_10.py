"""
QUESTÃO 10:
Conta espaços e vogais. Dado uma string com uma frase informada pelo
usuário (incluindo espaços em branco), conte: quantos espaços em branco
existem na frase. quantas vezes aparecem as vogais a, e, i, o, u.
"""


str1 = input('Digite um texto qualquer: ') .lower()
print('No seu texto, existem',  str1. count(' '), end= '')
print(' espaços')
print('No seu texto, existem', str1. count('a'), end= '')
print(' letras a')
print('No seu texto, existem', str1. count('e'), end='')
print(' letras e')
print('No seu texto, existem', str1. count('i'), end='')
print(' letras i')
print('No seu texto, existem', str1. count('o'), end='')
print('letras o')
print('No seu texto, existem', str1. count('u'), end='')
print('letras u')
 
