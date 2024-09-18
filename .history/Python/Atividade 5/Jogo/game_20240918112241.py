
#pip install pygame

import pygame
import random

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 000, 000)

largura_tela = 400
altura_tela = 500

imagem_nave = pygame.image.load("nave.png")
imagem_asteroide = pygame.image.load("asteroide.png")
imagem_asteroide = pygame.transform.scale(imagem_asteroide, (70,50))

imagem_nave = pygame.transform.scale(imagem_nave, (70,50))



class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = imagem_nave  # Use a imagem carregada aqui
        self.rect = self.image.get_rect()
        self.rect.x = largura_tela // 2
        self.rect.y = altura_tela - 50
        self.velocidade_x = 0


    def update(self):
        self.rect.x += self.velocidade_x
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > largura_tela - self.rect.width:
            self.rect.x = largura_tela - self.rect.width


class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([random.randint(20, 50), random.randint(20, 50)])
        self.image.fill(PRETO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura_tela - self.rect.width)
        self.rect.y = -self.rect.height
        self.velocidade_y = random.randint(1, 5)

    def update(self):
        self.rect.y += self.velocidade_y
        if self.rect.y > altura_tela:
            self.kill()


def reinicia_jogo():
    global pontuacao, velocidade_obstaculos, jogador, obstaculos
    pontuacao = 0
    velocidade_obstaculos = 3
    jogador.rect.x = largura_tela // 2
    jogador.rect.y = altura_tela - 50
    for obstaculo in obstaculos:
        obstaculo.kill()


pygame.init()

tela = pygame.display.set_mode([largura_tela, altura_tela])
pygame.display.set_caption("Desviar de Obstáculos")

todos_sprites = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()
jogador = Jogador()
todos_sprites.add(jogador)

fonte = pygame.font.Font(None, 36)

pontuacao = 0

velocidade_obstaculos = 3

clock = pygame.time.Clock()

terminou = False

#loop inicial
while not terminou:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminou = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jogador.velocidade_x = -5
            elif evento.key == pygame.K_RIGHT:
                jogador.velocidade_x = 5
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT and jogador.velocidade_x < 0:
                jogador.velocidade_x = 0
            elif evento.key == pygame.K_RIGHT and jogador.velocidade_x > 0:
                jogador.velocidade_x = 0

    #obstáculos aleatórios
    if random.randint(0, 100) < 2:
        obstaculo = Obstaculo()
        todos_sprites.add(obstaculo)
        obstaculos.add(obstaculo)

    todos_sprites.update()
    
    
    if pygame.sprite.spritecollide(jogador, obstaculos, False):
        reinicia_jogo()
    
    for obstaculo in obstaculos:
        if obstaculo.rect.y > jogador.rect.y:
            pontuacao += 10
            obstaculo.kill()
    
    if pontuacao % 500 == 0 and pontuacao != 0:
        velocidade_obstaculos += 1

    # desenha os sprites na tela
    tela.fill(BRANCO)
    todos_sprites.draw(tela)
    
    texto = fonte.render("Pontuação: " + str(pontuacao), True, PRETO)
    tela.blit(texto, [10, 10])

    # atualiza a tela
    pygame.display.flip()

    # define a velocidade de atualização do jogo
    clock.tick(60)
    
pygame.quit()
