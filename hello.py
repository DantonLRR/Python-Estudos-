a = "Danton";
b = "Lucas"
#  operacoes com string  como objetos
concatenar = a+ " "+ b;
print (concatenar)
print(concatenar.lower())
print(concatenar.upper())
print (concatenar)
#aplicando funcoes direto no objeto 
concatenar = concatenar.upper()
print (concatenar)
nova_string = "o rato roeu a roupa do rei de Roma"
minha_lista = nova_string.split("r")
#case sensitive
print(minha_lista)

busca = nova_string.find("rei")
print(busca)

nova_string2 = nova_string.replace("o rei", "a rainha");
print(nova_string2)