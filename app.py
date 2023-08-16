import pygame
from sys import exit

pygame.init()

window_x = 800
window_y = 400

window = pygame.display.set_mode((window_x, window_y))
window_rect = window.get_rect(topleft=(0, 0))
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 30)

# graphics

score_txt = font.render("Score :", False, "white")
score_rect = score_txt.get_rect(topleft=(120, 30))
lives_surf = font.render("9 Lives", False, "white")
lives_rect = lives_surf.get_rect(topright=(window_x-120, 30))


backdrop_surf = pygame.image.load("graphics/backdrop.png").convert()

floor_surf = pygame.image.load("graphics/floor.png").convert()
floor_rect = floor_surf.get_rect(bottomleft=(0, window_y))

grass_surf = pygame.image.load("graphics/grass.png").convert_alpha()
grass_rect = grass_surf.get_rect(bottomleft=(0, floor_rect.top + 50))

cat_surf = pygame.image.load("graphics/cat.png").convert_alpha()
cat_rect = cat_surf.get_rect(bottomleft=(100, floor_rect.top))

dog_surf = pygame.image.load("graphics/dog.png").convert_alpha()
dog_rect = dog_surf.get_rect(bottomleft=(600, floor_rect.top))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.blit(backdrop_surf, (0, 0))
    window.blit(score_txt, score_rect)
    window.blit(lives_surf, lives_rect)

    window.blit(floor_surf, floor_rect)
    window.blit(cat_surf, cat_rect)
    window.blit(dog_surf, dog_rect)

    grass_rect.left -= 1
    if grass_rect.left <= -800:
        grass_rect.left = 0
    window.blit(grass_surf, grass_rect)

    pygame.draw.line(window, "red", (0, 0), (window_x, window_y), 4)

    pygame.display.update()
    clock.tick(60)
