str = input('Digite um texto qualquer: ')
L1 = input('Digite a letra L1: ')
L2 = input('Digite a letra L2: ')
str2 = ''
for x in str:
    if x == L1: 
        x = L2
    elif x == L2: 
        x = L1
    str2 += x
print(str2)
