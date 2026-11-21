import pygame
pygame.init()
screen = pygame.display.set_mode((134 , 197))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (135 , 149 , 172), pygame.Rect(34 , 34 , 97 , 97))
    pygame.display.flip()
