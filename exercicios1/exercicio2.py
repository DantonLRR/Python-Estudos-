#Faça um programa que receba duas notas digitadas pelo usuário. 
# Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   
def somaNotas(x,y):
    return (x+y)

nota1 = int(input("Digite a primeira nota: "));
nota2 = int(input("Digite a segunda nota: "));
notaTotal = somaNotas(nota1,nota2);
print("nota total:", notaTotal)
if notaTotal >= 6:
    print("Aprovado")
else:
    print("Reprovado")