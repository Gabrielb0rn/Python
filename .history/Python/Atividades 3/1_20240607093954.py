print('\n---------------------------')
print("Bem-vindo(a) à Sorveteria!")
print('---------------------------')


sabores = []


while True:
    print("\nEscolha uma opção:\n1- Adicionar sabor\n2- Remover sabor\n3- Visualizar sorvete\n4- Finalizar pedido\n")
    opcao = input('Digite a opção selecionada: ')


    if opcao == '1':
        if len(sabores) < 4:
            sabor = input("Digite o sabor que você deseja adicionar: ")
            sabores.append(sabor)
            print("Sabor adicionado!")
        else:
            print("Limite de sabores atingido, remova um sabor!")
   
    elif opcao == '2':
        if sabores:
            sabor_removido = sabores.pop()
            print(f"Sabor {sabor_removido} removido!")
        else:
            print("Não existem sabores adicionados!")
   
    elif opcao == '3':
        if sabores:
            print("Seu sorvete possui os seguintes sabores:")
            for i, sabor in enumerate(sabores):
                print(f"Camada {i+1} - Sabor {sabor}")
        else:
            print("Seu sorvete não possui sabores!")
   
    elif opcao == '4':
        if sabores:
            print("Pedido realizado!")
            break
        else:
            print("Adicione pelo menos um sabor!")
   
    else:
        print("Opção inválida! Escolha uma opção válida.")
