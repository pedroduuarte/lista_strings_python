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
