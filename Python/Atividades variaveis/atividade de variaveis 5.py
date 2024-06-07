#Uma cidade pretende apurar os votos de sua eleição.
#1 Faça um programa para ler o número total de eleitores. Em seguida o número de votos do candidato X,
# o número de votos do candidato Y, total de votos brancos e total de votos nulos
#(a soma desses quatro, deve ser igual ao total de eleitores).
#2 Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

print(" ")
eleitores = input ("Quantidade de votos totais: ")

y = input("Votos em y: ")
x = input("Votos em x ")
b = input("Votos em branco: ")
n = input("Votos em nulo: ")

ry = int(100) * int(y) / int(eleitores)  

rx = int(100) * int(x) / int(eleitores)  

rb = int(100) * int(b) / int(eleitores)  

rn = int(100) * int(n) / int(eleitores)  

print(" ")
print("Votos em Y: ", ry, "%", "Votos em X: ", rx, "%", "Brancos: ", rb, "%", "Nulos: ", rn, "%.")

# x0