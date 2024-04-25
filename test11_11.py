"""
QUESTÃO 11:
Escreva um programa que leia uma string e imprima quantas vezes cada
caractere aparece nessa string.  String: TTAAC
 Formato de saída:
 T: 2x
 A: 2x
 C: 1x"""

str1 = input('Digitre uma string qualquer: ') .upper()
str2 = ''
for x in str1:  
   if x not in str2: 
      str2 += x
for x in str2: 
   print(f'{x}: {str1. count(x)} x')
