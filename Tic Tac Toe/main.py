import pygame

pygame.init()

screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()