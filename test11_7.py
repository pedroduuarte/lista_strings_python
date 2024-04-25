birth = input('Digite aqui a sua data de nascimento(no formato dd/mm/aaaa): ') .split('/')

if len(birth[0]) != 2: 
    print('Você digitou a data em um formato inválido, certifique-se que ela está no formato dd/mm/aaaa')
elif len(birth[1])  != 2: 
    print('Você digitou a data em um formato inválido, certifique-se que ela está no formato dd/mm/aaaa')
elif len(birth[2]) != 4: 
    print('Você digitou a data em um formato inválido, certifique-se que ela está no formato dd/mm/aaaa')

if birth[1] == '01': 
    birth[1] = 'Janeiro'
elif birth[1] == '02': 
    birth[1] = 'Fevereiro'
elif birth[1] == '03': 
    birth[1] = 'Março'
elif birth[1] == '04': 
    birth[1] = 'Abril'
elif birth[1] == '05': 
    birth[1] = 'Maio'
elif birth[1] == '06': 
    birth[1] = 'Junho'
elif birth[1] == '07': 
    birth[1] = 'Julho'
elif birth[1] == '08': 
    birth[1] = 'Agosto'
elif birth[1] == '09': 
    birth[1] = 'Setembro'
elif birth[1] == '10': 
    birth[1] = 'Outubro'
elif birth[1] == '11': 
    birth[1] = 'Novembro'
elif birth[1] == '12': 
    birth[1] = 'Dezembro'
else: print('Você digitou um mês inexistente')  

print(f'A sua data de nascimento é: {birth[0]} de {birth[1]} de {birth[2]}')
