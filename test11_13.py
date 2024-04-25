s = input('Digite um texto: ')
s2 = ''
for i in s:
    s2 += chr(ord(i)+1) 
print(s2)