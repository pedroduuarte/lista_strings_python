str1 = input('Digite algo: ') .upper()
str2 = input('Digite algo: ') .upper()
str3 = ''
for i in str1: 
    if i in str2 and i not in str3: 
        str3 += i
print(f'1ª string: {str1}')
print(f'2ª string: {str2}')
print(f'3ª string: {str3}')