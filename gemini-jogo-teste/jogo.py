import random

def jogar_adivinhacao():

  print("Bem-vindo ao jogo de adivinhação!")
  numero_secreto = random.randint(1, 100)
  tentativas = 0
  limite_tentativas = 5

  print("Estou pensando em um número entre 1 e 100.")

  while tentativas < limite_tentativas:
    try:
      palpite = int(input(f"Tentativa {tentativas + 1}/{limite_tentativas}: Digite um número: "))
    except ValueError:
      print("Por favor, digite um número válido.")
      continue

    tentativas += 1

    if palpite < numero_secreto:
      print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
      print("Muito alto! Tente novamente.")
    else:
      print(f"Parabéns! Você acertou em {tentativas} tentativas.")
      return

  print(f"Você esgotou as tentativas. O número secreto era {numero_secreto}")

if __name__ == "__main__":
  jogar_adivinhacao()