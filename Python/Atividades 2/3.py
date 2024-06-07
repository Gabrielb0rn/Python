hpCastelo = 500
rodadas = 0


while hpCastelo > 0:
    print(f"HP do castelo: {hpCastelo}")


    print("Escolha uma opção:")
    print("1) Ataque Bomba (-100HP)")
    print("2) Ataque Granada (-80HP)")
    print("3) Ataque Arqueiro (-40HP)")
    print("4) Defesa Escudo (+20HP)")


    opcao = input("Opção escolhida: ")


    if opcao == "1":
        hpCastelo -= 100
    elif opcao == "2":
        hpCastelo -= 80
    elif opcao == "3":
        hpCastelo -= 40
    elif opcao == "4":
        hpCastelo += 20
    else:
        print("Opção inválida. Tente novamente.")
        continue


    rodadas += 1


print(f"Jogo encerrado, com {rodadas} rodadas!")


# x0