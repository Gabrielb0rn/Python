import matplotlib.pyplot as plt


data = {'Despacito': 8 , 'Shape of You': 6 , 'See You Again': 5.9, 'UpTown Funk ': 4.9, 'Gangnam Style ': 4.8}


plt.bar(data.keys(), data.values())


# Adicionar título e rótulos aos eixos
plt.title('5 das músicas mais vistas do YouTube [Atualizado em 2023]:')
plt.xlabel('Músicas')
plt.ylabel('Reproduções (Em bilhões)')


plt.show()

# x0