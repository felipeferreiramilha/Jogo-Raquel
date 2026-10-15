pip install pygame
import random
import sys
import pygame

# Inicialização do Pygame
pygame.init()

# Configurações da Tela
WIDTH, HEIGHT = 800, 600
FPS = 60

# Cores Temáticas do Espaço
BLACK = (5, 5, 15)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 50, 50)
PURPLE = (180, 50, 255)

# Janela do Jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Big Bang: A Expansão do Universo")
clock = pygame.time.Clock()

# Fontes
font = pygame.font.SysFont(None, 32)
large_font = pygame.font.SysFont(None, 56)


class Player:

  def __init__(self):
    self.x = WIDTH // 2
    self.y = HEIGHT // 2
    self.radius = 16
    self.speed = 6

  def move(self, keys):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
      self.x -= self.speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
      self.x += self.speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
      self.y -= self.speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
      self.y += self.speed

    # Limites da tela
    self.x = max(self.radius, min(WIDTH - self.radius, self.x))
    self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

  def draw(self, surface):
    # Efeito de brilho da singularidade
    pygame.draw.circle(
        surface, (0, 100, 255), (int(self.x), int(self.y)), self.radius + 8
    )
    pygame.draw.circle(
        surface, CYAN, (int(self.x), int(self.y)), self.radius
    )


class CosmicParticle:

  def __init__(self, is_danger=False):
    self.x = random.randint(20, WIDTH - 20)
    self.y = random.randint(20, HEIGHT - 20)
    self.is_danger = is_danger
    self.radius = random.randint(10, 15) if is_danger else random.randint(6, 10)
    self.dx = random.choice([-2, -1, 1, 2])
    self.dy = random.choice([-2, -1, 1, 2])

  def update(self):
    self.x += self.dx
    self.y += self.dy
    # Rebater nas bordas
    if self.x < 0 or self.x > WIDTH:
      self.dx *= -1
    if self.y < 0 or self.y > HEIGHT:
      self.dy *= -1

  def draw(self, surface):
    color = RED if self.is_danger else YELLOW
    pygame.draw.circle(
        surface, color, (int(self.x), int(self.y)), self.radius
    )


def main():
  player = Player()
  particles = []
  score = 0
  stability = 3
  spawn_timer = 0

  running = True
  while running:
    screen.fill(BLACK)

    # Tratamento de Eventos
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    # Movimentação do Jogador
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Geração de Partículas do Universo
    spawn_timer += 1
    if spawn_timer > 25:
      spawn_timer = 0
      # 30% de chance de ser Antimatéria/Entropia (perigo)
      is_danger = random.random() < 0.3
      particles.append(CosmicParticle(is_danger))

    # Atualizar e Desenhar Partículas
    for p in particles[:]:
      p.update()
      p.draw(screen)

      # Detecção de Colisão
      dist = ((player.x - p.x) ** 2 + (player.y - p.y) ** 2) ** 0.5
      if dist < player.radius + p.radius:
        if p.is_danger:
          stability -= 1
          particles.remove(p)
          if stability <= 0:
            running = False
        else:
          score += 10
          particles.remove(p)
          # A cada 50 pontos, a expansão cresce um pouco
          if player.radius < 35 and score % 50 == 0:
            player.radius += 1

    # Desenhar Jogador
    player.draw(screen)

    # Interface do Usuário (HUD)
    score_text = font.render(f"Matéria Absorvida: {score}", True, WHITE)
    stability_text = font.render(
        f"Estabilidade do Universo: {stability}", True, RED
    )
    screen.blit(score_text, (20, 20))
    screen.blit(stability_text, (20, 55))

    pygame.display.flip()
    clock.tick(FPS)

  # Tela de Fim de Jogo (Colapso Cósmico)
  while True:
    screen.fill(BLACK)
    over_text = large_font.render("COLAPSO CÓSMICO (FIM)", True, RED)
    final_score = font.render(
        f"Pontuação Final: {score} - Pressione ESC para Sair", True, WHITE
    )

    screen.blit(
        over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 3)
    )
    screen.blit(
        final_score, (WIDTH // 2 - final_score.get_width() // 2, HEIGHT // 2)
    )

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(FPS)


if __name__ == "__main__":
  main()
