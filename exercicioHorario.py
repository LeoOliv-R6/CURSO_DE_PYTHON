"""-------------------Exercicio 2-------------------"""
# horas = float(input('Digite um horario: '))

# if horas >= 0 or horas <= 11:
#     print('Bom dia!')
# elif horas >= 12 or horas <= 17:
#     print('Boa tarde!')
# else:
#     print('Boa noite!')
    
    
entrada = input('Digite um horario: ')

try:
    hora = float(entrada)
    
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Não conheço esse horario!')
except:
    print('Horario invalido!')