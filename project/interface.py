import pygame
from principalBuscaSemPesosGrid import Gera_Problema
from buscaGridNP import buscaGridNP
from principalBuscaSemPesosGrid import Get_Origin
from principalBuscaSemPesosGrid import Get_Destiny
import random

def move_character_with_image(screen, grid, current_pos, target_x, target_y, cell_size, character_image):
    """
    Move um personagem com imagem pela grid de forma animada.

    Parâmetros:
    - screen: Superfície do pygame onde o personagem será desenhado.
    - grid: Matriz representando a grid do jogo.
    - current_pos: Tupla (x, y) da posição atual do personagem.
    - target_x, target_y: Coordenadas destino dentro da grid.
    - cell_size: Tamanho da célula da grid.
    - character_image: Superfície Pygame com a imagem do personagem.

    Retorna:
    - Nova posição do personagem após a movimentação.
    """
    x, y = current_pos

    # Se a posição alvo for um obstáculo, não move
    if grid[target_y][target_x] == 9:
        return x, y  # Retorna a posição atual

    # Converte coordenadas da grid para pixels
    start_x, start_y = x * cell_size, y * cell_size
    end_x, end_y = target_x * cell_size, target_y * cell_size

    # Quantidade de frames para a animação
    frames = 5 * 60;
    for i in range(frames):
        interp_x = start_x + (end_x - start_x) * (i / frames)
        interp_y = start_y + (end_y - start_y) * (i / frames)

        # Redesenha a tela
        screen.fill((0, 0, 0))  # Limpa fundo

        # Redesenha grid
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                color = (255, 255, 255) if grid[i][j] == 0 else (255, 0, 0)
                pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))
                pygame.draw.rect(screen, (0, 0, 0), (j * cell_size, i * cell_size, cell_size, cell_size), 1)

        # Desenha a imagem do personagem no centro da célula
        char_rect = character_image.get_rect(center=(int(interp_x + cell_size // 2), int(interp_y + cell_size // 2)))
        screen.blit(character_image, char_rect)

        pygame.display.flip()
        pygame.time.delay(20)  # Pequena pausa para suavizar animação

    return target_x, target_y  # Atualiza a posição do personagem

# Configurações da tela
sol = buscaGridNP()
caminho = []

person_pos = Get_Origin();

pygame.init()
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Tamanho da grid
cell_size = 50
rows, cols = 10, 10  # Número de células
nx  = 5
ny  = 5
qtd = 5
# Gerar tabela aleatória (0 = caminho livre, 9 = obstáculo)
grid = Gera_Problema(nx, ny, qtd); # Função que gera o problema
character_image = pygame.image.load("PR_ATO.png")
character_image = pygame.transform.scale(character_image, (40,40))

new_x, new_y = 4,3 
fullscreen = False
running = True
print("-------------------")
print(grid)
print("-------------------")
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
    cell_size = min(width // ny, height // nx)

    for i in range(nx):
        for j in range(ny):
            if grid[i][j] == 0:
                color = (255, 255, 255)  # Branco → Caminho livre
            else:
                color = (255, 0, 0)  # Vermelho → Obstáculo (9)

            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, (0, 0, 0), (j * cell_size, i * cell_size, cell_size, cell_size), 1)
    person_pos = move_character_with_image(screen, grid, person_pos, new_x, new_y, cell_size, character_image)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()