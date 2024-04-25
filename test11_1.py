"""
QUESTÃO 1:
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do
seu comprimento. Informe também se as duas strings possuem o mesmo
comprimento e são iguais ou diferentes no conteúdo.
"""
str1 = input('Digite aqui uma texto qualquer: ')
str2 = input('Digite aqui mais um texto: ')     
print(str1[0:])
print( '=== ' 'COMPRIMENTO: ',len(str1)) 
print(str2[0:])
print('=== ''COMPRIMENTO: ',len(str2))

if str1 == str2: 
    print('Os dois textos possuem o mesmo conteúdo.')
else: print('Os dois textos NÃO possuem o mesmo conteúdo.')
