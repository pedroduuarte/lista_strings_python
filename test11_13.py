"""
QUESTÃO 13:
Faça um programa que leia uma palavra e some 1 no valor ASCII de cada
caractere da palavra. Imprima a string resultante.  Dica: O Python disponibiliza 2 funções que são bastante uteis quando estamos
trabalhando com o sistema ASCII. A primeira é a função ord() , que recebe uma
letra como parâmetro e retorna o código ASCII da mesma. A segunda função, é a
chr() , onde passamos o código ASCII e nos é retornado a respectiva letra."""

s = input('Digite um texto: ')
s2 = ''
for i in s:
    s2 += chr(ord(i)+1) 
print(s2)