a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
# Variavel recebe os valores parametrizados para armazenar os dados
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}' # 2f -> casas decimais

# O .alguma coisa, assim como o .format, são métodos, detro do método está o argumento.
# Isso serve para tratar o dado
# variavel recebe o valor referenciado
formato = string.format(
    # parametro recebe variavel
    nome1=a, nome2=b, nome3=c
)

print(formato)