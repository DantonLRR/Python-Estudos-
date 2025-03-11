#funcao Map
#aplica uma funcao a cada item da lista
def dobro(x):
    return x*2

valor =[1,2,3,4,5,6]

valor_dobrado = map(dobro, valor)


#cria uma lista com os valores dobrados
valor_dobrado2 = list(valor_dobrado )
print(valor_dobrado2 )