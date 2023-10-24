"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome? Digite:')
    print(f'Seu nome é {nome}')
    perg = input('Deseja continuar?')
    
    if perg == 'Não':
        print('Obrigado!')
        break
    