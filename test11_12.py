"""
QUESTÃO 12:
Número por extenso. Escreva um programa que solicite ao usuário a
digitação de um número até 99 e imprima-o na tela por extenso."""
numbers = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
numbers2 = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
x = int(input('Digite um número de 1 a 99: '))
if x < 0 or x > 99:     
    print('Você digitou um número inválido!')
if x < 20: 
    resultado = numbers[x]
    print(resultado)
elif x >= 20 and x < 100:
    dezenas = x//10 
    unidades = x % 10
    resultado = numbers2[dezenas]
    if unidades == 0:
        print(f'{resultado}')
    else: print(f'{resultado} e {numbers[unidades]}')


