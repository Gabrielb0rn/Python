valorCompra = float(input("Digite o valor da compra: "))
categoria_assinante = int(input("Digite a categoria de assinante (1, 2, 3 ou 4): "))


if categoria_assinante == 1:
    valorCompra *= 0.8
    frete = 0
elif categoria_assinante == 2:
    valorCompra *= 0.8
    frete = 12.5
elif categoria_assinante == 3:
    valorCompra *= 0.9
    frete = 12.5
elif categoria_assinante == 4:
    frete = 12.5
else:
    print("Opção inválida!")
    exit()


valor_final = valorCompra + frete


print(f"Valor da compra: R${valorCompra:.2f}")
print(f"Valor do frete: R${frete:.2f}")
print(f"Valor final da compra: R${valor_final:.2f}")


# x0