import pygame 
import random
import sys
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000) #Fire event every 1000 milliseconds (1 second)
done = False
bg = (0, 0, 0)

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Ball colors
ballColor = (255, 0, 0) # Red

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('audio/catch.mp3')
bonus_sound = pygame.mixer.Sound('audio/bonus.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 

#Unbreakable brick settings
unbreakable_color = (100, 100, 100) #Grey
unbreakable_block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(1,11,2) for j in range(1,5,2)]

#Bonus brick settings
bonus_color = (0, 255, 0) #Green
bonus_block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(0,10,2) for j in range(0,4,2)]

#Add unbreakable and bonus bricks to block list
block_list = block_list + unbreakable_block_list + bonus_block_list
color_list = color_list + [unbreakable_color] * len(unbreakable_block_list) + [bonus_color] * len(bonus_block_list)

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Pause Screen
pausefont = pygame.font.SysFont('comicsansms', 40)
pausetext = pausefont.render('Paused - Press P to Resume', True, (255, 255, 255))
pausetextRect = pausetext.get_rect()
pausetextRect.center = (W // 2, H // 2)

# Transparent black surface
transparent_black = pygame.Surface((W, H), pygame.SRCALPHA)
transparent_black.fill((0, 0, 0, 30))  # Adjust the fourth value (alpha) for transparency

# Main Menu
main_menu_font = pygame.font.SysFont('comicsansms', 40)
main_menu_text = main_menu_font.render('Press SPACE to Start', True, (255, 255, 255))
main_menu_rect = main_menu_text.get_rect()
main_menu_rect.center = (W // 2, H // 2)

# Settings Screen
settings_font = pygame.font.SysFont('comicsansms', 40)
settings_img = pygame.image.load('images/Settings.png').convert_alpha()
settings_rect = settings_img.get_rect()
settings_rect.center = (W // 2, H // 2 - 50)
settings_text = settings_font.render('Press S to switch ball color and RETURN to resume', True, (0, 0, 0))
settingstextRect = settings_text.get_rect()
settingstextRect.center = (W // 2, H // 2 + 50)


paused = False
in_menu = True
in_settings = False

def main_menu():
    screen.fill((0, 0, 0))
    screen.blit(main_menu_text, main_menu_rect)
    pygame.display.flip()
    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                
def settings_menu():
    global in_settings, ballColor
    screen.fill((255, 255, 255))
    screen.blit(settings_img, settings_rect)
    screen.blit(settings_text, settingstextRect)
    pygame.display.flip()
    while in_settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s: # Switch ball color
                    ballColor = (0, 0, 255) #Blue
                elif event.key == pygame.K_RETURN:
                    in_settings = False
                    return

main_menu()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.USEREVENT:
            ballSpeed += 0.5
            if paddle.width != 0:
                paddle.width = paddleW - 1
                paddleW = paddle.width
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_RETURN and not in_settings:
                in_settings = True
                settings_menu()
     
    if paused:
        screen.blit(transparent_black, (0, 0))  # Blit the transparent black surface
        screen.blit(pausetext, pausetextRect)
        pygame.display.flip()
        clock.tick(FPS)
        continue

    screen.fill(bg)
    
    # print(next(enumerate(block_list)))
    
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)] #drawing blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(ballColor), ball.center, ballRadius)
    # print(next(enumerate (block_list)))

    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy



    #Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    #Collision blocks
    hitIndex = ball.collidelist(block_list)
    
    if hitIndex != -1:
        hitRect = block_list[hitIndex]
        hitColor = color_list[hitIndex]
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        if hitColor != unbreakable_color: #Check if the collided block is not unbreakable
            block_list.pop(hitIndex)
            color_list.pop(hitIndex)
            if hitColor != bonus_color:
                game_score += 1
                collision_sound.play()
            elif hitColor == bonus_color:
                game_score += 5
                bonus_sound.play()
        
    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
    # print(pygame.K_LEFT)
    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed


    pygame.display.flip()
    clock.tick(FPS)