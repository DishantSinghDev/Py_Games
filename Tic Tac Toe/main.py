import pygame

pygame.init()

screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block Game")
player = pygame.Rect((0,0,20,20))

run = True

while run:
    # for filling the whole screen with black color whenever this loop runs to prevent the previous rectangle issue
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (225,225,225), player)

    # for rectangle movement
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_DOWN] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_LEFT] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT] == True:
        player.move_ip(1, 0)

    # for preventing the rectangle going outside the window
    if player.left < 0:
        player.left = 0
    if player.right > screen_width:
        player.right = screen_width
    if player.top < 0:
        player.top = 0
    if player.bottom > screen_height:
        player.bottom = screen_height
    

    # for quiting the window when the user presses the cross button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # for updating the screen as the whole loop runs
    pygame.display.update()

pygame.quit()