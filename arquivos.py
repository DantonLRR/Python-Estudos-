arquivo = open("arquivos/arquivo.txt");
#ler arquivos
linhas = arquivo.readlines();
print(linhas)
print("----")

for linha in linhas:
    print (linha)
print("----")

texto_completo = arquivo.read()
print(texto_completo)
#criar arquivo
#funcao open(arquivo, modo de abertura do arquivo)
#open("arquivo2.txt", "w") Abre o arquivo "meu_arquivo.txt" no modo de escrita, oque existia sera substituido
#open("meu_arquivo.txt", "r")Abre o arquivo "meu_arquivo.txt" no modo de leitura
#open("meu_arquivo.txt", "a")Abre o arquivo "meu_arquivo.txt" no modo de adição, oque adiciona um novo conteudo a oque ja existia


#w = open("arquivo2.txt", "w") arquivo criado, testando o uso do parametro "a" para adiçao
w = open("arquivos/arquivo2.txt", "a")
# Escreve "esse eh o meu arquivo" no arquivo
w.write("esse eh o meu arquivo\n")
#sempre que abrir um arquivo fechar ele
w.close()