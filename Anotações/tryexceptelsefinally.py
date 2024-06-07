nomeArquivo = 'arquivoUm.txt'

try:
    arquivo = open(nomeArquivo, 'r')

except FileNotFoundError:
    arquivo = open(nomeArquivo, 'a')

else:
    print(f"Arquivo {nomeArquivo} já existe")

finally:
    arquivo.close()