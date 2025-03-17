import pygame 
from pygame import mixer

pygame.init()
mixer.init()
pygame.display.set_caption("My player")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

FPS = 50
done = False
n = 0
musics = [r'C:\Users\Aspire 3\Desktop\PP2_labs\lab7\player\Adele_-_Love_In_The_Dark_47835146.mp3', r'C:\Users\Aspire 3\Desktop\PP2_labs\lab7\player\Adele_-_Lovesong_47835371.mp3', r'C:\Users\Aspire 3\Desktop\PP2_labs\lab7\player\Adele_-_Skyfall_48385024.mp3', r'C:\Users\Aspire 3\Desktop\PP2_labs\lab7\player\Adele_-_Someone_Like_You_47835372.mp3']
photo = [r'C:\Users\Aspire 3\Desktop\PP2_labs\lab7\player\lind.png', r'C:\Users\Aspire 3\Desktop\PP2_labs\lab7\player\lv.png', r'C:\Users\Aspire 3\Desktop\PP2_labs\lab7\player\Skyfall.png', r'C:\Users\Aspire 3\Desktop\PP2_labs\lab7\player\smly.png']
play = pygame.image.load(r'C:\Users\Aspire 3\Desktop\PP2_labs\lab7\player\play.png')
pausee = pygame.image.load(r'C:\Users\Aspire 3\Desktop\PP2_labs\lab7\player\pause.png')

def start(n):
    
    mixer.music.load(musics[n])
      
    mixer.music.set_volume(0.2)
    mixer.music.play()

start(n)

def update_track_image():
    global sm_photo
    loaded_photo = pygame.image.load(photo[n])
    sm_photo = pygame.transform.scale(loaded_photo, (500,500))

update_track_image()

w = play.get_width()
h = play.get_height()
play_sm =  pygame.transform.scale(play, ((w // 2)-170, (h // 2)-170))  


w = pausee.get_width()
h = pausee.get_height()
pause_sm =  pygame.transform.scale(pausee, ((w // 2)-170, (h // 2)-170))  


paused = False

while not done:  
    screen.fill((0, 0, 0))
    screen.blit(sm_photo, (150, 100))
    if not paused:
     screen.blit(play_sm, (350, 620))
    else: 
       screen.blit(pause_sm, (350,620))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            paused = not paused
            if paused:
                mixer.music.pause() 
            else:
                mixer.music.unpause()
            


        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if n == len(musics) - 1:  
                n = 0
            else: 
                n += 1 
            start(n)
            update_track_image() 

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if n == 0: 
             n = len(musics) - 1
            else: 
             n -= 1 
            start(n)
            update_track_image() 
  
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
