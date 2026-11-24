import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

image = pygame.image.load("hero.jpg")
image = pygame.transform.scale(image, (300, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((58, 58, 58))
    screen.blit(image, (100, 100))
    pygame.display.update()

