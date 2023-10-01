import pygame
pygame.init()

# Setting up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))  # Fill the window with a black color
    pygame.display.flip()

pygame.quit()