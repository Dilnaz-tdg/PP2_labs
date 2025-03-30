import pygame
import random
from color_palett import *  

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((HEIGHT, WIDTH))  #окно

CELL = 30  #клетка размер


def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

# шахматная сетка
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# точка
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]  # начальное тело
        self.dx = 1  # в начале идет вправо
        self.dy = 0

    def move(self): 
        for i in range(len(self.body) - 1, 0, -1):  
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx  # двигаем голову
        self.body[0].y += self.dy

    def draw(self):  
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))  # голова
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))  # тело

    def check_collision(self, food): 
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))  # тело больше на один 
            return True
        return False

# еда
class Food:
    def __init__(self, snake):
        while True:  
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            on_snake = False
            for segment in snake.body: #есть ли совпадение координат с телом змейки
                if segment.x == x and segment.y == y:
                    on_snake = True
                    break
            if not on_snake: # если место есть создаем еду
                self.pos = Point(x, y) # сохраняем позицию еды 
                break
        self.value = random.choice([1,3,5]) 
        self.spawn_time = pygame.time.get_ticks() #сохраняем момент времени появления еды


        if self.value == 1:
            self.color = colorGREEN
        elif self.value == 3:
            self.color = colorYELLOW
        elif self.value == 5:
            self.color = colorRED

    def draw(self):  # еда
        pygame.draw.rect(screen, self.color , (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

FPS = 5
score = 0
level = 1
clock = pygame.time.Clock()

snake = Snake()
food = Food(snake)

running = True
while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    draw_grid_chess()  

    snake.move() 

    current_time = pygame.time.get_ticks()
    if food.value == 5 and current_time - food.spawn_time > 5000:
       food = Food(snake) #новая еда 

    # проверка стены
    head = snake.body[0]
    if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
        print("Game Over: hit the wall")
        running = False

    # проверка на столкновение с собой
    for segment in snake.body[1:]:
        if head.x == segment.x and head.y == segment.y:
            print("Game Over: hit itself")
            running = False
            break

    # съели еду
    if snake.check_collision(food):
        score += food.value
        if score % 3 == 0:
            level += 1
            FPS += 1  # ускорение
        food = Food(snake)

    snake.draw()
    food.draw()

    # вывод счёта и уровня
    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {score}", True, colorBLACK)
    level_text = font.render(f"Level: {level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
