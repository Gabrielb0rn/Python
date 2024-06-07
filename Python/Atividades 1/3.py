soma_idades = 0




for i in range(5):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))


   
    soma_idades += idade


media_idades = soma_idades / 5


print(f"A soma das idades é {soma_idades}.")
print(f"A média das idades é {media_idades:.2f}.")


# x0