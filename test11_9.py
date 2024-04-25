"""
"QUESTÃO 9:
Escreva um programa que leia duas strings e gere uma terceira com os
caracteres comuns às duas strings lidas.  1a string: AAACTBF
 2a string: CBT
 Resultado: CBT
 A ordem dos caracteres da string gerada não é importante, mas deve
conter todas as letras comuns a ambas.
"""

str1 = input('Digite algo: ') .upper()
str2 = input('Digite algo: ') .upper()
str3 = ''
for i in str1: 
    if i in str2 and i not in str3: 
        str3 += i
print(f'1ª string: {str1}')
print(f'2ª string: {str2}')
print(f'3ª string: {str3}')