primeiroValor = input('Digite um valor: ')
segundoValor = input('Digite outro valor: ')

if primeiroValor > segundoValor:
    print('O primeiro valor inserido', primeiroValor, 'é maior que o segundo valor ',segundoValor)
elif primeiroValor == segundoValor:
    print('Os dois valores inseridos são iguais:', primeiroValor, 'e' ,segundoValor)
else: 
    print('O segundo valor inserido', segundoValor, 'é maior que o primeiro valor', primeiroValor)
