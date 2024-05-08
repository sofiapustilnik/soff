# Abre um novo arquivo, escreve e fecha
with open('outro_arquivo.txt', 'w') as arquivo:
    arquivo.write('Outro exemplo\ncom novos dados')

# Reabre o arquivo para leitura e escrita
with open('outro_arquivo.txt', 'r+') as arquivo:
    conteudo = arquivo.read()  # Lê o conteúdo do arquivo
    arquivo.seek(0)  # Retorna ao início do arquivo
    print(arquivo.read())  # Imprime o conteúdo novamente
# Abre o arquivo para escrita, acrescenta uma nova linha e fecha
with open('novo_arquivo.txt', 'a') as arquivo:
    arquivo.write('\nNunca é demais')

# Reabre o arquivo para leitura
with open('novo_arquivo.txt', 'r') as arquivo:
    print(arquivo.read())  # Imprime o conteúdo do arquivo
# Abre o arquivo para leitura
with open("novo_arquivo.txt", "r") as arquivo:
    # Itera sobre cada linha no arquivo e imprime
    for linha in arquivo:
        print(linha)

    # Retorna ao início do arquivo
    arquivo.seek(0)

    # Itera novamente sobre cada linha no arquivo e imprime sem adicionar nova linha
    for linha in arquivo:
        print(linha, end='')
def gravar_nome():
    nome = input("Por favor, digite seu nome: ")
    with open("nome_usuario.txt", "w") as arquivo:
        arquivo.write(nome)
def imprimir_conteudo_arquivo():
    nome_arquivo = input("Por favor, digite o nome do arquivo: ")
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
def copiar_conteudo():
    with open("arquivo_origem.txt", "r") as arquivo_origem:
        conteudo = arquivo_origem.read()
    with open("arquivo_destino.txt", "w") as arquivo_destino:
        arquivo_destino.write(conteudo)
def imprimir_nome_por_numero():
    numero = int(input("Por favor, digite um número: "))
    with open("arquivo_exemplo.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        nome = linhas[numero - 1].strip()  # -1 porque os índices começam em 0
        print(nome)


