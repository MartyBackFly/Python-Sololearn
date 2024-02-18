import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("no se game ")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Jugador
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

# Gravedad
fall_speed = 0
gravity = 1

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # Aplicar gravedad al jugador
    fall_speed += gravity
    player_y += fall_speed

    # Verificar colisiones con el suelo
    if player_y > height - player_size:
        player_y = height - player_size
        fall_speed = 0

    # Limpiar la pantalla
    screen.fill(black)

    # Dibujar al jugador
    pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(30)
