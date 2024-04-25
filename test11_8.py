"""
QUESTÃO 8:
Escreva um programa que leia duas strings. Verifique se a segunda ocorre
dentro da primeira e imprima a posição de início.  1a string: AABBEFAATT
 2a string: BE
 Resultado: BE encontrado na posição 3 de AABBEFAATT"""

str1 = input('Digite um texto qualquer: ') .upper()
str2 = input('Digite outro texto qualquer: ') .upper()
print(f'{str2} encontrado na {str1. find(str2)}ª posição do primeiro texto.')
