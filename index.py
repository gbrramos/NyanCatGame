import pygame
from pygame import font
pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("AAAAAAAAAAAAAAAAAAA")

x = 328
y = 276
vel = 12

back = pygame.image.load('img/bg.jpg')
nyan = pygame.image.load('img/nyan.gif')
back_size = pygame.transform.scale(back,(800,600))
nyan_small = pygame.transform.scale(nyan,(150,100))

open_window = True
while open_window:

    pygame.time.delay(50)

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            open_window = False

    commands = pygame.key.get_pressed()
    if commands[pygame.K_UP] or commands[pygame.K_w]:
        y = y - vel
    if commands[pygame.K_DOWN] or commands[pygame.K_s]:
        y = y + vel
    if commands[pygame.K_RIGHT] or commands[pygame.K_d]:
        x = x + vel
    if commands[pygame.K_LEFT] or commands[pygame.K_a]:
        x = x - vel    
    window.blit(back_size,(0,0))
    window.blit(nyan_small,(x,y))
   
    # pygame.font.init()                              
    # fontesys1 = pygame.font.SysFont(x, 60)      
    # fontesys2 = pygame.font.SysFont(y, 60)                
    # txttela = fontesys.render(txt, 1, (255,255,255))  
    # window.blit(txttela,(10,10))   
    # window.blit(txttela,(10,10))                      
    # pygame.font.get_default_font()
    pygame.display.flip()
pygame.quit()