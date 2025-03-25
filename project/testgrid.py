import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
clock = pygame.time.Clock()

fullscreen = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:  # Alternar modo tela cheia
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
            elif event.key == pygame.K_ESCAPE:  # Sair com ESC
                running = False

    screen.fill((255, 255, 255))

    width, height = screen.get_size()
    cell_size = 50

    for i in range(0, width, cell_size):
        pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, height))
    for j in range(0, height, cell_size):
        pygame.draw.line(screen, (0, 0, 0), (0, j), (width, j))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()