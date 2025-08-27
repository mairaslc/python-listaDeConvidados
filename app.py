convidados_da_festa = ['Maria','João','Ana','Carlos','Mariana']

status_presenca = {}

print('--- verificação da lista de convidados ---')

lista_de_chegada = ['joão','Ana','Carlos','Maria']

for pessoa in lista_de_chegada:
    if pessoa in convidados_da_festa:
        print(f'olá, {pessoa}! Bem-vindo(a) á festa.')
        status_presenca[pessoa] = "Confirmado"
    else:
        print(f'Desculpa, {pessoa}. Seu nome não está na lista')
        status_presenca[pessoa] = 'Não convidado'
