import pygame

class Cube:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.enabled = True

    def draw(self, screen):
        if self.enabled:
            pygame.draw.rect(screen, self.color, self.rect)

    def move(self, dx, dy, screen_width, screen_height, cub2, cub3, cub4, cub5, speed):
        new_rect = self.rect.move(dx * speed, dy * speed)

        if new_rect.left < 0 or new_rect.right > screen_width:
            dx = -dx
        if new_rect.top < 0 or new_rect.bottom > screen_height:
            dy = -dy

        if cub2.enabled and new_rect.colliderect(cub2.rect):
            dx = -dx
            dy = -dy
        if cub3.enabled and new_rect.colliderect(cub3.rect):
            dx = -dx
            dy = -dy
        if cub4.enabled and new_rect.colliderect(cub4.rect):
            dx = -dx
            dy = -dy
        if cub5.enabled and new_rect.colliderect(cub5.rect):
            dx = -dx
            dy = -dy

        self.rect.x += dx * speed
        self.rect.y += dy * speed

pygame.init()
pygame.mixer.music.load("win_sound.mp3")

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Кубы
cub2 = Cube(90, 54, 80, 720, (0, 0, 0))
cub3 = Cube(270, 1, 80, 540, (0, 0, 0))
cub4 = Cube(450, 54, 80, 720, (0, 0, 0))
cub5 = Cube(630, 1, 80, 540, (0, 0, 0))
cub6 = Cube(710, 20, 90, 50, (255,255,0))
cube = Cube(20, 520, 50, 50, (255, 0, 0))  # игрок

# Иконка и заголовок
pygame.display.set_caption("GAME")
pygame.display.set_icon(pygame.image.load("icon.png"))

# Состояние
running = True
speed = 2
font = pygame.font.SysFont(None, 48)
show_text = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    keys = pygame.key.get_pressed()
    dx = dy = 0
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        dy = -1
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        dy = 1

    cube.move(dx, dy, 800, 600, cub2, cub3, cub4, cub5, speed)

    if cube.rect.colliderect(cub6.rect):
        pygame.mixer.music.play(loops=999)
        cub2.enabled = False
        cub3.enabled = False
        cub4.enabled = False
        cub5.enabled = False
        speed = 20
        show_text = True
        


    screen.fill((255, 255, 255))
    cub2.draw(screen)
    cub3.draw(screen)
    cub4.draw(screen)
    cub5.draw(screen)
    cub6.draw(screen)
    cube.draw(screen)

    if show_text:
        text = font.render("Ты прошёл!", True, (0, 128, 0))
        screen.blit(text, (300, 260))

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
