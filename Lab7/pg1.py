import pygame
import datetime

pygame.init()

screen_width, screen_height = 800, 800
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Mouse Clock")
clock = pygame.time.Clock()
FPS = 60

clock_image = pygame.image.load("mainclock.png").convert_alpha()
right_arm_image = pygame.image.load("rightarm.png").convert_alpha()
left_arm_image = pygame.image.load("leftarm.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    current_time = datetime.datetime.now()
    minute = current_time.minute
    second = current_time.second

    display.fill((255, 255, 255))
    display.blit(clock_image, (screen_width // 2 - clock_image.get_width() // 2, screen_height // 2 - clock_image.get_height() // 2))

    rotated_right_arm = pygame.transform.rotate(right_arm_image, -minute * 6)
    rotated_left_arm = pygame.transform.rotate(left_arm_image, -second * 6)

    display.blit(rotated_right_arm, (screen_width // 2 - rotated_right_arm.get_width() // 2, screen_height // 2 - rotated_right_arm.get_height() // 2))
    display.blit(rotated_left_arm, (screen_width // 2 - rotated_left_arm.get_width() // 2, screen_height // 2 - rotated_left_arm.get_height() // 2))

    pygame.display.update()
    clock.tick(FPS)