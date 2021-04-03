import pygame
from pygame import font

pygame.init()
pygame.font.init()                              

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Nyan Cat's New Adventure")

x = 328
y = 276
vel = 12

back = pygame.image.load('img/bg.jpg')
nyan = pygame.image.load('img/nyan.gif')
back_size = pygame.transform.scale(back,(800,600))
nyan_small = pygame.transform.scale(nyan,(150,100))

music = pygame.mixer.music.load('tmp/bg-sound-nyan-trap-remix.mp3')
pygame.mixer.music.set_volume(0.07)
pygame.mixer.music.get_volume()
pygame.mixer.music.play(10)

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

    strX = 'X: '+str(x)
    strY = 'Y: '+str(y)

    fontX = pygame.font.SysFont(strX, 30)      
    fontY = pygame.font.SysFont(strY, 30)                
    txtX = fontX.render(strX, 1, (255,255,255))  
    txtY = fontY.render(strY, 1, (255,255,255))  
    window.blit(txtX,(10,10))   
    window.blit(txtY,(10,40))    
    pygame.font.get_default_font()
    pygame.display.flip()
pygame.quit()