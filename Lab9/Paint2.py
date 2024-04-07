import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    shape_mode = 'circle'
    points = []
    
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # determine the shape
                if event.key == pygame.K_1:
                    shape_mode = 'rectangle'
                elif event.key == pygame.K_2:
                    shape_mode = 'circle'
                elif event.key == pygame.K_3:
                    shape_mode = 'square'
                elif event.key == pygame.K_4:
                    shape_mode = 'right triangle'
                elif event.key == pygame.K_5:
                    shape_mode = 'equilateral triangle'
                elif event.key == pygame.K_6:
                    shape_mode = 'rhombus'


                # determine the color
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e: #Press 'e' to switch eraser mode
                    mode = 'eraser'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, shape_mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode, shape_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'eraser':
        color = (0, 0, 0)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])        
        if shape_mode == 'circle':
            pygame.draw.circle(screen, color, (x, y), width)
        elif shape_mode == 'rectangle':
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width*2, width*4))
        elif shape_mode == 'square':
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width*2, width*2))
        elif shape_mode == 'right triangle':
            triangle_vertices = [(x, y), (x, y + width*2 ), (x + width*2, y + width*2)]
            pygame.draw.polygon(screen, color, triangle_vertices)
        elif shape_mode == 'equilateral triangle':
            height = math.sqrt(3)/2 * width  #Height of the triangle
            triangle_vertices = [(x, y - height), (x - width, y + height), (x + width, y + height)]
            pygame.draw.polygon(screen, color, triangle_vertices)
        elif shape_mode == 'rhombus':
            height = width*3
            vertices = [(x, y - height/2), (x + width, y), (x, y + height/2), (x - width, y)]
            pygame.draw.polygon(screen, color, vertices)

main()