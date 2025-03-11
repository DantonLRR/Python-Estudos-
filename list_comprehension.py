#lista comprehension
#fazer com com y receba os valores de x ao quadrado 
x= [1,2,3,4]
#y=[valor_a_adicionar laço condicao]
y=[i**2 for i in x]
print (y)
#pegar os numeros impares da lista x
z=[i for i in x if i%2==1]
print(z)