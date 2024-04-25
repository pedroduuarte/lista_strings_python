str1 = input('Digite aqui uma string qualquer: ') .replace(' ','') .upper() .replace('Ô','O') .replace('Â','A') .upper() 
str2 = str1[::-1]
if str1 == str2: 
    print('É UM PALÍNDROMO!')
else: print('NÃO É UM PALÍNDROMO!')