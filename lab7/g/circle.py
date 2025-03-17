import pygame

pygame.init()

WIDTH = 800
HEIGHT = 480
screen = pygame.display.set_mode((800, 480))

COLOR_white = (255,255,255)
COLOR_red = (255,0,0)

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

movement_speed = 20
circle_radius = 25

running = True 

clock = pygame.time.Clock()
FPS = 60 

while running:

    screen.fill(COLOR_white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
    
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_UP] and circle_y - circle_radius - movement_speed >= 0:
        circle_y -= movement_speed
    if pressed_keys[pygame.K_DOWN] and  circle_y + circle_radius + movement_speed <= HEIGHT:
        circle_y += movement_speed
    if pressed_keys[pygame.K_RIGHT] and circle_x + circle_radius + movement_speed <= WIDTH:
        circle_x += movement_speed
    if pressed_keys[pygame.K_LEFT] and circle_x - circle_radius - movement_speed >= 0:
        circle_x -= movement_speed
    

    pygame.draw.circle(screen, COLOR_red, (circle_x, circle_y), 25)
    
    

    pygame.display.flip()
    clock.tick(FPS)


