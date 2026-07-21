import pygame

pygame.init()
screen_width = 800
screen_height = 600
screeen = pygame.display.set_mode((screen_width, screen_height))
is_running=True
bg_color=(23,243,123)
player_x=375
player_y=200
while is_running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            is_running=False
    screeen.fill(bg_color)
    player_rect=pygame.Rect(player_x, player_y,50,50)
    pygame.draw.rect(screeen,"dark green", player_rect)
    player_rect2=pygame.Rect(360, 250,80,160)
    pygame.draw.rect(screeen,"dark green", player_rect2)
    pygame.display.flip()

pygame.quit()



