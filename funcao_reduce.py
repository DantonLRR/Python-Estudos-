#funcao reduce
#soma valres da lista
from functools import reduce

def soma(x,y):
    return x+y
lista =[1,3,5,10,20]

soma= reduce(soma,lista)
print(soma)