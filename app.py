import pygame
from sys import exit
import math
from random import randint

pygame.init()

# Set display width and height
window_x = 800
window_y = 400

# Main game settings
window = pygame.display.set_mode((window_x, window_y))
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 30)
font_lg = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
last_time_ticks = 0
cat_gravity = 0
score = 0

# graphics
backdrop_surf = pygame.image.load("graphics/backdrop.png").convert()

floor_surf = pygame.image.load("graphics/floor.png").convert()
floor_rect = floor_surf.get_rect(bottomleft=(0, window_y))

grass_surf = pygame.image.load("graphics/grass.png").convert_alpha()
grass_rect = grass_surf.get_rect(bottomleft=(0, floor_rect.top + 50))

cat_surf = pygame.image.load("graphics/cat.png").convert_alpha()
cat_rect = cat_surf.get_rect(bottomleft=(100, floor_rect.top))

dog_surf = pygame.image.load("graphics/dog.png").convert_alpha()
dog_rect = dog_surf.get_rect(bottomleft=(600, floor_rect.top))

# obsticles
obstacle_rect_list = []

# timer
obsticle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obsticle_timer, 1200)


def obstacle_movement(obstacle_rect_list):
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            obstacle_rect.x -= 10
            window.blit(dog_surf, obstacle_rect)


def drawScore():
    time_now = int((pygame.time.get_ticks() / 1000) - last_time_ticks)
    score_surf = font.render(f"My Score {time_now}", "false", "white")
    score_rect = score_surf.get_rect(topleft=(50, 50))
    window.blit(score_surf, score_rect)
    return time_now


def gameOver():
    window.fill((13, 60, 79))
    player_surf = pygame.transform.rotozoom(cat_surf, 0, 2)
    player_rect = player_surf.get_rect(center=(window_x/2, window_y/2))

    score_title = font_lg.render(
        "Kitty Kat", False, "White")
    score_title_rect = score_title.get_rect(center=(window_x/2, 70))

    info_title = font.render("Press SPACE to play!", False, "White")
    info_title_rect = info_title.get_rect(center=(window_x/2, 330))

    final_title = font.render(
        f"Your score is {score}. Press SPACE to play again!!", False, "White")
    final_title_rect = final_title.get_rect(center=(window_x/2, 330))

    window.blit(score_title, score_title_rect)
    window.blit(player_surf, player_rect)

    if score == 0:
        window.blit(info_title, info_title_rect)
    else:
        window.blit(final_title, final_title_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if cat_rect.bottom == floor_rect.top and event.key == pygame.K_SPACE:
                    cat_gravity = -25

            if cat_rect.bottom == floor_rect.top and event.type == pygame.MOUSEBUTTONDOWN:
                if cat_rect.collidepoint(event.pos):
                    cat_gravity = -25

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                dog_rect.left = window_x
                game_active = True
                last_time_ticks = int(pygame.time.get_ticks())/1000

        if event.type == obsticle_timer and game_active:
            obstacle_rect_list.append(dog_surf.get_rect(
                bottomleft=(randint(900, 1900), floor_rect.top)))

    # Main game loop
    if game_active:

        # Update score variable
        score = drawScore()

        # Backdrop
        window.blit(backdrop_surf, (0, 0))

        # Score
        drawScore()

        # Floor
        window.blit(floor_surf, floor_rect)

        # Grass
        grass_rect.left -= 1
        if grass_rect.left <= -800:
            grass_rect.left = 0
        window.blit(grass_surf, grass_rect)

        # Cat
        cat_gravity += 1
        cat_rect.y += cat_gravity
        if cat_rect.bottom >= floor_rect.top:
            cat_rect.bottom = floor_rect.top
        window.blit(cat_surf, cat_rect)

        # Obstacle movement
        obstacle_movement(obstacle_rect_list)

        # Dog
        # dog_rect.left -= 5
        # if dog_rect.right <= 0:
        #     dog_rect.left = window_x
        # window.blit(dog_surf, dog_rect)

        # Check Cat / Dog collision
        if cat_rect.colliderect(dog_rect):
            game_active = False
            dog_rect.right = window_x

    else:

        gameOver()

    pygame.display.update()
    clock.tick(60)
