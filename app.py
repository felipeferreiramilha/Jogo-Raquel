import pygame
import random
import syslibsdl2-dev
libsdl2-image-dev
libsdl2-mixer-dev
libsdl2-ttf-dev
libportmidi-dev
libfreetype6-dev

# Inicialização do Pygame
pygame.init()

# Dimensões da tela
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("CDZ: A Batalha do Cosmo - Cosmologia")

# Cores (Padrão Cosmos / Cavaleiros)
PRETO = (10, 10, 25)
AZUL_COSMO = (0, 150, 255)
DOURADO = (255, 215, 0)
ROXO_ESCURO = (75, 0, 130)
BRANCO = (255, 255, 255)
VERMELHO = (220, 20, 60)

# Fonte
FONTE = pygame.font.SysFont("arial", 20)
FONTE_GRANDE = pygame.font.SysFont("arial", 32, bold=True)

class Cavaleiro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 50))
        self.image.fill(DOURADO) # Representando a armadura dourada
        self.rect = self.image.get_rect(center=(100, ALTURA // 2))
        self.velocidade = 6

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and self.rect.top > 50:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.bottom < ALTURA - 20:
            self.rect.y += self.velocidade
        if teclas[pygame.K_LEFT] and self.rect.left > 20:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < LARGURA - 20:
            self.rect.x += self.velocidade

class MateriaEscura(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(ROXO_ESCURO) # Matéria escura invisível/misteriosa
        self.rect = self.image.get_rect(
            x=random.randint(LARGURA, LARGURA + 300),
            y=random.randint(60, ALTURA - 50)
        )
        self.velocidade = random.randint(3, 7)

    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.rect.x = random.randint(LARGURA + 50, LARGURA + 300)
            self.rect.y = random.randint(60, ALTURA - 50)

class AnomaliaBigBang(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(VERMELHO) # Radiação / Instabilidade
        self.rect = self.image.get_rect(
            x=random.randint(LARGURA, LARGURA + 400),
            y=random.randint(60, ALTURA - 50)
        )
        self.velocidade = random.randint(5, 9)

    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.rect.x = random.randint(LARGURA + 100, LARGURA + 500)
            self.rect.y = random.randint(60, ALTURA - 50)

def jogo():
    relogio = pygame.time.Clock()
    
    jogador = Cavaleiro()
    todos_sprites = pygame.sprite.Group(jogador)
    
    grupo_materia = pygame.sprite.Group()
    for _ in range(5):
        m = MateriaEscura()
        grupo_materia.add(m)
        todos_sprites.add(m)

    grupo_anomalias = pygame.sprite.Group()
    for _ in range(3):
        a = AnomaliaBigBang()
        grupo_anomalias.add(a)
        todos_sprites.add(a)

    pontos_materia = 0
    estabilidade_cosmos = 100
    executando = True

    while executando:
        TELA.fill(PRETO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Atualizações
        todos_sprites.update()

        # Colisões com Matéria Escura
        colisoes_materia = pygame.sprite.spritecollide(jogador, grupo_materia, True)
        for colisao in colisoes_materia:
            pontos_materia += 1
            estabilidade_cosmos = min(100, estabilidade_cosmos + 10)
            novo_m = MateriaEscura()
            grupo_materia.add(novo_m)
            todos_sprites.add(novo_m)

        # Colisões com Anomalias (Big Bang descontrolado)
        colisoes_anomalia = pygame.sprite.spritecollide(jogador, grupo_anomalias, True)
        for colisao in colisoes_anomalia:
            estabilidade_cosmos -= 25
            nova_a = AnomaliaBigBang()
            grupo_anomalias.add(nova_a)
            todos_sprites.add(nova_a)

        # Condição de Fim de Jogo
        if estabilidade_cosmos <= 0:
            executando = False

        # Desenhar elementos na tela
        todos_sprites.draw(TELA)

        # Interface (HUD)
        texto_pontos = FONTE.render(f"Matéria Escura Coletada: {pontos_materia}", True, BRANCO)
        texto_cosmos = FONTE.render(f"Estabilidade do Cosmo: {estabilidade_cosmos}%", True, DOURADO)
        texto_instrucao = FONTE.render("Use as setas para mover o Cavaleiro e absorver a Matéria Escura!", True, AZUL_COSMO)
        
        TELA.blit(texto_pontos, (20, 15))
        TELA.blit(texto_cosmos, (450, 15))
        TELA.blit(texto_instrucao, (20, ALTURA - 30))

        pygame.display.flip()
        relogio.tick(60)

    # Tela de Game Over
    TELA.fill(PRETO)
    texto_fim = FONTE_GRANDE.render("O COSMO COLAPSOU!", True, VERMELHO)
    texto_sub = FONTE.render("A instabilidade do Big Bang superou a Matéria Escura.", True, BRANCO)
    TELA.blit(texto_fim, (LARGURA // 2 - 170, ALTURA // 2 - 40))
    TELA.blit(texto_sub, (LARGURA // 2 - 210, ALTURA // 2 + 10))
    pygame.display.flip()
    pygame.time.wait(4000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    jogo()
