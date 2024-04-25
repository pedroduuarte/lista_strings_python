"""QUESTÃO 5:
Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da
direita para esquerda ou vice-versa. Por exemplo: OSSO e OVO são palíndromos. Em
textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO
ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre-a e diga se é um
palíndromo ou não."""

str1 = input('Digite aqui uma string qualquer: ') .replace(' ','') .upper() .replace('Ô','O') .replace('Â','A') .upper() 
str2 = str1[::-1]
if str1 == str2: 
    print('É UM PALÍNDROMO!')
else: print('NÃO É UM PALÍNDROMO!')