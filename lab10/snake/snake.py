import pygame
import random
from color_palett import *  
import psycopg2
import datetime

def create_tables():
    conn = psycopg2.connect(
        host="localhost",
        port=5433,
        database="postgres",
        user="postgres",
        password="12345"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER,
            level INTEGER,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Tables checked/created successfully.")

pygame.init()

def get_user_info():
    conn = psycopg2.connect(
        host="localhost",
        port=5433,
        database="postgres",
        user="postgres",
        password="12345"
    )
    cur = conn.cursor()

    username = input("Enter your username: ")

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
        cur.execute("SELECT MAX(level) FROM user_score WHERE user_id = %s", (user_id,))
        level_row = cur.fetchone()
        if level_row and level_row[0]:
            print(f"Welcome back, {username}! Your last level was {level_row[0]}.")
            return user_id, level_row[0]
        else:
            return user_id, 1
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        print(f"Welcome, {username}!")
        return user_id, 1

create_tables()
user_id, level = get_user_info()

WIDTH, HEIGHT, CELL = 600, 600, 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

def draw_walls(level):
    wall_color = (0, 0, 0)
    wall_coords = []
    if level >= 3:
        wall_coords += [(9, y) for y in range(8, 12)]
    if level >= 4:
        wall_coords += [(0, y) for y in range(0, 20)]
    if level >= 5:
        wall_coords += [(19, y) for y in range(0, 20)]
    if level >= 6:
        wall_coords += [(x, 3) for x in range(1, 4)]
    if level >= 7:
        wall_coords += [(x, 10) for x in range(1, 4)]
    if level >= 8:
        wall_coords += [(x, 16) for x in range(1, 4)]
    if level >= 9:
        wall_coords += [(x, 3) for x in range(16, 19)]
    if level >= 10:
        wall_coords += [(x, 10) for x in range(16, 19)]
    if level >= 11:
        wall_coords += [(x, 16) for x in range(16, 19)]
    for (x, y) in wall_coords:
        pygame.draw.rect(screen, wall_color, (x * CELL, y * CELL, CELL, CELL))
    return wall_coords

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            return True
        return False

class Food:
    def __init__(self, snake, walls):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            on_snake = any(segment.x == x and segment.y == y for segment in snake.body)
            on_wall = (x, y) in walls
            if not on_snake and not on_wall:
                self.pos = Point(x, y)
                break
        self.value = random.choice([1,3,5])
        self.spawn_time = pygame.time.get_ticks()
        self.color = {1: colorGREEN, 3: colorYELLOW, 5: colorRED}[self.value]

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

FPS = 5
score = 0
clock = pygame.time.Clock()
snake = Snake()
walls = draw_walls(level)
food = Food(snake, walls)
running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1; snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1; snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0; snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0; snake.dy = -1
            elif event.key == pygame.K_SPACE:
                paused = True
                print("Game paused. Press SPACE to continue.")
                conn = psycopg2.connect(
                    host="localhost", port=5433, database="postgres",
                    user="postgres", password="12345"
                )
                cur = conn.cursor()
                cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
                            (user_id, score, level))
                conn.commit()
                cur.close(); conn.close()
                print("Progress saved to database.")
                while paused:
                    for ev in pygame.event.get():
                        if ev.type == pygame.QUIT:
                            paused = False; running = False
                        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                            paused = False

    draw_grid_chess()
    snake.move()

    current_time = pygame.time.get_ticks()
    if food.value == 5 and current_time - food.spawn_time > 5000:
        food = Food(snake, walls)

    head = snake.body[0]
    if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
        print("Game Over: hit the wall")
        running = False

    for segment in snake.body[1:]:
        if head.x == segment.x and head.y == segment.y:
            print("Game Over: hit itself")
            running = False

    walls = draw_walls(level)
    for (x, y) in walls:
        if head.x == x and head.y == y:
            print("Game Over: hit a wall")
            running = False

    if snake.check_collision(food):
        score += food.value
        if score % 3 == 0:
            level += 1
            FPS += 1
        walls = draw_walls(level)
        food = Food(snake, walls)

    snake.draw()
    food.draw()
    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {score}", True, colorBLACK)
    level_text = font.render(f"Level: {level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
