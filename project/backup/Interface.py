import pygame
from GridSearchNoWeight import Gera_Problema
from project.depraced.GridSearch import buscaGridNP
from GridSearchNoWeight import Get_Origin
from GridSearchNoWeight import Get_Destiny

import pygame
import random

def move_character_with_image(screen, grid, person_pos, new_x, new_y, cell_size, character_image):
    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0:
        person_pos = (new_x, new_y)
    x, y = person_pos[1] * cell_size, person_pos[0] * cell_size
    screen.blit(character_image, (x + (cell_size - 40) // 2, y + (cell_size - 40) // 2))
    return person_pos

pygame.init()
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Tamanho da grid
cell_size = 50
nx, ny = 5, 5  # Número de células
qtd = 5

# Grid já gerado anteriormente
grid = Gera_Problema(nx, ny, qtd)

character_image = pygame.image.load("PR_ATO.png")
character_image = pygame.transform.scale(character_image, (40, 40))

new_x, new_y = 4, 3
fullscreen = False
running = True
person_pos = (new_x, new_y)

# Calcula o tamanho da célula uma única vez
width, height = screen.get_size()
cell_size = min(width // ny, height // nx)

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
                # Recalcular tamanho da célula após redimensionamento
                width, height = screen.get_size()
                cell_size = min(width // ny, height // nx)
            elif event.key == pygame.K_ESCAPE:  # Sair com ESC
                running = False
            elif event.key == pygame.K_UP:
                new_x, new_y = person_pos[0] - 1, person_pos[1]
            elif event.key == pygame.K_DOWN:
                new_x, new_y = person_pos[0] + 1, person_pos[1]
            elif event.key == pygame.K_LEFT:
                new_x, new_y = person_pos[0], person_pos[1] - 1
            elif event.key == pygame.K_RIGHT:
                new_x, new_y = person_pos[0], person_pos[1] + 1

    screen.fill((0, 0, 0))  # Fundo preto

    # Desenhar apenas a grid (evitando cálculos repetitivos)
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            color = (255, 255, 255) if cell == 0 else (255, 0, 0)
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, (0, 0, 0), (j * cell_size, i * cell_size, cell_size, cell_size), 1)

    # Mover e desenhar personagem
    person_pos = move_character_with_image(screen, grid, person_pos, new_x, new_y, cell_size, character_image)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
