#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.  
def operacaoEscolhida(num1,num2,sinal):
    if sinal == "+":
        return num1 + num2
    elif sinal == "-":
        return num1 - num2
    elif sinal == "*":
        return num1 * num2
    else:
        return "Erro: sinal inválido!"

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
sinal = input("digite o sinal para operacao: ")

operacao = operacaoEscolhida(num1,num2,sinal)

print(operacao);