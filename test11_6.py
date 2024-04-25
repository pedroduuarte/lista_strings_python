"""QUESTÃO 6: 
Faça uma função que recebe uma string que representa uma cadeia de DNA e gera a
cadeia complementar. A entrada e saída de dados deve ser feita pelo programa
principal.  Exemplo:
 Entrada: AATCTGCAC
 Saída: TTAGACGTG
"""

s = input('Escreva aqui a cadeia DNA: ') .upper()
chain = ''
correct = True
for i in range (len(s)):
    dna = s[i]
    if dna == 'A':
        chain += 'T'
    elif dna == 'T':
        chain += 'A'
    elif dna == 'C':
        chain += 'G'
    elif dna == 'G':
        chain += 'C'
    else:  
        correct = False
        break 
if correct:
    print(f'Essa é a sua cadeia complementar: {chain}')
else: print('Você digitou uma cadeia inválida!')
