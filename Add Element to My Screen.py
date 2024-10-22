import pygame

pygame.init()

screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Color Changing Sprite 420")

colors = {
    'red': pygame.Color('red'),
    'green': pygame.Color('green'),
    'blue': pygame.Color('blue'),
    'yellow': pygame.Color('yellow'),
    'white': pygame.Color('white')
}
current_color = colors['white']

x, y = 30, 30
sprite_width, sprite_height = 60, 60

clock = pygame.time.Clock()

font = pygame.font.SysFont("Times New Roman", 36)
text = font.render("My First Game Screen", True, (158, 16, 16))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    
    x = min(max(0, x), screen_width - sprite_width)
    y = min(max(0, y), screen_height - sprite_height)
    
    if x == 0: current_color = colors["blue"]
    elif x == screen_width - sprite_width: current_color = colors["yellow"]
    elif y == 0: current_color = colors["red"]
    elif y == screen_height - sprite_height: current_color = colors["green"]
    else: current_color = colors["white"]
    
    screen.fill((0, 0, 0))
    
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, 50))
    
    pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
    
    pygame.display.flip()
    clock.tick(90)
    
pygame.quit()
