import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(0, 500, 50):
        pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 500))
        pygame.draw.line(screen, (0, 0, 0), (0, i), (500, i))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
