senha = input("Digite a senha: ")
confirmacao = input("Digite a senha novamente: ")


while senha != confirmacao:
    print("As senhas não correspondem. Tente novamente.")
    senha = input("Digite a senha: ")
    confirmacao = input("Digite a senha novamente: ")


print("As senhas correspondem!")


# x0