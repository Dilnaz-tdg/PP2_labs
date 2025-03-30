import pygame
import random
import time

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # окно


image_background = pygame.image.load('AnimatedStreet.png') # все фото
image_player = pygame.image.load('Player.png')
image_enemy = pygame.image.load('Enemy.png')
image_coin_1 = pygame.image.load('c.png')
image_coin_3 = pygame.image.load('c3.png')
image_coin_5 = pygame.image.load('c5.png')
image_coin_1 = pygame.transform.scale(image_coin_1, (40, 40))
image_coin_3 = pygame.transform.scale(image_coin_3, (50, 50))
image_coin_5 = pygame.transform.scale(image_coin_5, (60, 60))

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1) # всегда играет

sound_crash = pygame.mixer.Sound('crash.wav') # короткий звук 

coin_sound = pygame.mixer.Sound('coinsound.mp3')

score = 0
score_font = pygame.font.SysFont('Verdana', 20)

coinscore = 0
coint_font = pygame.font.SysFont('Verdana', 20)

last_coin_milestone = 0


font = pygame.font.SysFont("Verdana", 60)
image_game_over = font.render("Game Over", True, 'black')
image_game_over_rect = image_game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2 # по центру по х
        self.rect.bottom = HEIGHT # снизу по у
        self.speed = 5



    def move(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0) # вправо
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0) # влево 
        if self.rect.left < 0: # границы
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 10

    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w) # случайное появление по х
        self.rect.bottom = 0
    
    def move(self):
        self.rect.move_ip(0, self.speed) # движение вниз по у
        if self.rect.top > HEIGHT:
            self.generate_random_rect() # перезапуск сверху 
            global score 
            score += 1

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin_1
        self.rect = self.image.get_rect()
        self.speed = 10
        self.value = 1
        self.generate_random_coin()
    def generate_random_coin(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0 # появляется сверху 

        self.value = random.choice([1, 3, 5]) 

        if self.value == 1:
            self.image = image_coin_1
        elif self.value == 3:
            self.image = image_coin_3
        elif self.value == 5:
            self.image = image_coin_5
        
        self.rect = self.image.get_rect(left=self.rect.left, bottom=self.rect.bottom) #сохраняем координату

    def move(self):
        self.rect.move_ip(0, self.speed) # движение вниз по у 
        if self.rect.top > HEIGHT:
            self.generate_random_coin()



running = True

clock = pygame.time.Clock()
FPS = 60

player = Player() # создаем объекты 
enemy = Enemy()
coin = Coins()


all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add(player,enemy,coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if coinscore - last_coin_milestone >= 5:
            enemy.speed += 0.5 
            last_coin_milestone = coinscore

    player.move()

    screen.blit(image_background, (0,0))

    score_text = score_font.render(f"Score: {score}", True, 'black')
    screen.blit(score_text, (10,10))

    coinscore_text = score_font.render(f"coins: {coinscore}", True, 'black')
    screen.blit(coinscore_text, (300 ,10))
    

    for entity in all_sprites: # движение всех объектов 
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, coin_sprites):
        coin_sound.play()
        coinscore += coin.value
        coin.generate_random_coin()
    
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)

        running = False 
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()

        time.sleep(3)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()





