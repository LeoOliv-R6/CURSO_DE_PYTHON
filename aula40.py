"""While/else"""
string = input('Digite algo que não seja números:')

i = 0 
while i < len(string):
    letra = string[i]
    
    if letra == '':
        break
    
    print(letra)
    i += 1
else:
    print('O else foi executado')
print('Fora do while')
    