import pygame
import datetime


pygame.init()


WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")
clock = pygame.time.Clock()


clock_surf= pygame.image.load(r"C:\Users\Aspire 3\Desktop\PP2_labs\lab7\cl\clock.png")  
minute_hand = pygame.image.load(r"C:\Users\Aspire 3\Desktop\PP2_labs\lab7\cl\min_hand.png") 
second_hand = pygame.image.load(r"C:\Users\Aspire 3\Desktop\PP2_labs\lab7\cl\sec_hand.png")  


center_x =  WIDTH // 2
center_y =  HEIGHT // 2

clock_rect = clock_surf.get_rect(center = (center_x, center_y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    minute = now.minute
    second = now.second

    angle_minute = - (minute * 6 - 90)
    angle_second = - (second * 6 - 90)  
    
    rotated_minute = pygame.transform.rotate(minute_hand, angle_minute)
    rotated_second = pygame.transform.rotate(second_hand, angle_second)
    
    minute_rect = rotated_minute.get_rect(center=(center_x, center_y))
    second_rect = rotated_second.get_rect(center=(center_x, center_y))
    
    screen.fill((255,255,255))
    screen.blit(clock_surf, clock_rect) 
    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_second, second_rect.topleft)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
