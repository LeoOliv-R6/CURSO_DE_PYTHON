nome = 'Leonardo'
altura = 1.80
peso = 91
imc = peso / altura ** 2

"f-strings" # -> permite que eu coloque variaveis dentro de variaveis  
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987