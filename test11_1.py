str1 = input('Digite aqui uma texto qualquer: ')
str2 = input('Digite aqui mais um texto: ')     
print(str1[0:])
print( '=== ' 'COMPRIMENTO: ',len(str1)) 
print(str2[0:])
print('=== ''COMPRIMENTO: ',len(str2))

if str1 == str2: 
    print('Os dois textos possuem o mesmo conteúdo.')
else: print('Os dois textos NÃO possuem o mesmo conteúdo.')
