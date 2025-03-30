import pygame

pygame.init()

COLOR_white = (255, 255, 255)
COLOR_green = (34, 139, 34)
COLOR_blue = (0, 0, 255)
COLOR_red = (255, 0, 0)
eraser = (0, 0, 0)


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

radius = 10
mode = COLOR_white
last_pos = None

def drawCircle(screen, mouse_pos, color):
    x, y = mouse_pos
    pygame.draw.circle(screen, color, (x, y), 90, 3)

def drawLineBetween(screen, start, end, width, color_mode):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color_mode, (x, y), width)

def drawRectangle(screen, mouse_pos, w, h, color):
    x, y = mouse_pos
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)


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


