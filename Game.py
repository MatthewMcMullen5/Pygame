import pygame
# following https://www.youtube.com/watch?v=Vlolidaoiak

pygame.init()

# game window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('')

# load images
# background image
background_image = pygame.image.load('images/Backgrounds/background.jpeg').convert_alpha()
# panel image
panel_image = pygame.image.load('images/Backgrounds/background.jpeg').convert_alpha()


# function for drawing background
def draw_bg():
    screen.blit(background_image, (0, 0))


# function for drawing panel image
def draw_panel():
    screen.blit(panel_image, (0, screen_height - bottom_panel))


run = True
while run:
    # draw background and panel
    draw_bg()
    draw_panel()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
