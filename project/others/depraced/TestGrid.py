import pygame
import random

# Configurações da tela
pygame.init()
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Tamanho da grid
cell_size = 50
rows, cols = 10, 10  # Número de células

# Gerar tabela aleatória (0 = caminho livre, 9 = obstáculo)
grid = Gera_Problema(nx, ny, qtd); # Função que gera o problema

fullscreen = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:  # Alternar tela cheia
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
            elif event.key == pygame.K_ESCAPE:  # Sair com ESC
                running = False

    screen.fill((0, 0, 0))  # Fundo preto

    # Obter tamanho da tela e calcular células
    width, height = screen.get_size()
    cell_size = min(width // cols, height // rows)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                color = (255, 255, 255)  # Branco → Caminho livre
            else:
                color = (255, 0, 0)  # Vermelho → Obstáculo (9)

            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, (0, 0, 0), (j * cell_size, i * cell_size, cell_size, cell_size), 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()