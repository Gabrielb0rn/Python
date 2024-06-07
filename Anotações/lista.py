numeros = []
#         0    1   2   3   4   5   6   7
idades = [15, 22, 14, 31, 20, 22, 15, 18]
nomes = []
#            0         1        2       3          4         5
cores = ['Amarelo', 'Verde', 'Roxo', 'Verde', 'Vermelho', 'Azul']

corAdd = input('Cor a adicionar: ')
cores.append(corAdd)
cores.pop(0)
print(cores)

# corPesquisa = input('Cor a pesquisar: ')

# for color in cores:
#     if corPesquisa == color:
#         print("Encontrouuuu")


# for color in cores:
#     print(color)

#print(idades[len(idades)-1])

# print(len(numeros))
# print(len(idades))

# print(max(idades))
# print(min(idades))

#print(max(cores))