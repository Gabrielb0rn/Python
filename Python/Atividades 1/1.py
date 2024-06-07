distancia = float(input("Digite a distância percorrida em quilômetros: "))
tipoCarro = input("Digite o tipo do carro (A, B ou C): ")


if tipoCarro == "A":
    consumoMedio = distancia / 8
    print(f"A média estimada de consumo de combustível é de {consumoMedio:.2f} litros.")
elif tipoCarro == "B":
    consumoMedio = distancia / 12
    print(f"A média estimada de consumo de combustível é de {consumoMedio:.2f} litros.")
elif tipoCarro == "C":
    consumoMedio = distancia / 9
    print(f"A média estimada de consumo de combustível é de {consumoMedio:.2f} litros.")
else:
    print("Tipo de carro inválido!")


# x0