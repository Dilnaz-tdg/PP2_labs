import pygame
import math

pygame.init()

COLOR_white = (255, 255, 255)
COLOR_green = (34, 139, 34)
COLOR_blue = (0, 0, 255)
COLOR_red = (255, 0, 0)
eraser = (0, 0, 0)


screen = pygame.display.set_mode((640, 480)) #экран
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

radius = 10
mode = COLOR_white
last_pos = None

def drawCircle(screen, mouse_pos, color):
    x, y = mouse_pos 
    pygame.draw.circle(screen, color, (x, y), 90, 3) # радиус 90, толщина 3 

def drawLineBetween(screen, start, end, width, color_mode):
    dx = start[0] - end[0] #разность координат по х
    dy = start[1] - end[1] #по у 
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations): #отрисовка кругами
        progress = i / iterations #от 0 - 1 
        aprogress = 1 - progress # обратно
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color_mode, (x, y), width) # рисуем круг

def drawRectangle(screen, mouse_pos, w, h, color):
    x, y = mouse_pos # верхний левый угол
    rect = pygame.Rect(x, y, w, h) # прямоугольник
    pygame.draw.rect(screen, color, rect, 3) 

def drawSquare(screen, mouse_pos, w, h, color):
    x, y = mouse_pos
    rect = pygame.Rect(x, y, w, h) 
    pygame.draw.rect(screen, color, rect, 3)

def drawRightTriangle(screen, mouse_pos, width, height, color):
    x, y = mouse_pos
    point1 = (x, y) #первый угол          
    point2 = (x + width, y) #второй угол      
    point3 = (x, y + height) #третий угол      
    pygame.draw.polygon(screen, color, [point1, point2, point3], 3)  


def drawEquilateralTriangle(screen, mouse_pos, side_length, color):
    x, y = mouse_pos 
    height = (math.sqrt(3) / 2) * side_length #высота треугольника 

    point1 = (x, y)  #верхняя точка
    point2 = (x - side_length / 2, y + height)  #нижняя левая
    point3 = (x + side_length / 2, y + height)  #нижняя правая

    pygame.draw.polygon(screen, color, [point1, point2, point3], 3)

def drawRhombus(screen, mouse_pos, width, height, color):
    x, y = mouse_pos
    top = (x, y - height // 2) #верхняя 
    right = (x + width // 2, y) #правая
    bottom = (x, y + height // 2) #нижняя
    left = (x - width // 2, y) #левая

    pygame.draw.polygon(screen, color, [top, right, bottom, left], 3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                mode = COLOR_red
            elif event.key == pygame.K_g:
                mode = COLOR_green
            elif event.key == pygame.K_b:
                mode = COLOR_blue
            elif event.key == pygame.K_BACKSPACE:
                mode = eraser
            elif event.key == pygame.K_w:
                drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, mode)
            elif event.key == pygame.K_c:
                drawCircle(screen, pygame.mouse.get_pos(), mode)
            elif event.key == pygame.K_s:
                drawSquare(screen, pygame.mouse.get_pos(), 100, 100, mode)
            elif event.key == pygame.K_t:
                drawRightTriangle(screen, pygame.mouse.get_pos(), 100, 100, mode)
            elif event.key == pygame.K_y:
                drawEquilateralTriangle(screen, pygame.mouse.get_pos(), 100, mode)
            elif event.key == pygame.K_u:
                drawRhombus(screen, pygame.mouse.get_pos(), 100, 50, mode)


        #левая кнопка мыши
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            last_pos = pygame.mouse.get_pos()

        #с нажатой левой кнопкой
        if event.type == pygame.MOUSEMOTION and event.buttons[0]:
            if last_pos is not None:
                start_pos = last_pos
                end_pos = pygame.mouse.get_pos()
                drawLineBetween(screen, start_pos, end_pos, radius, mode)
                last_pos = end_pos

    pygame.display.flip()
    clock.tick(60)


