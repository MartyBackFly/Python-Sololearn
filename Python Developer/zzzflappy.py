import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Jugador (pájaro)
bird_size = 30
bird_x = width // 4
bird_y = height // 2
bird_speed = 5
gravity = 1

# Obstáculos
obstacle_width = 50
obstacle_height = random.randint(100, height - 100)
obstacle_x = width
obstacle_speed = 5
space_between_obstacles = 150

# Puntuación
score = 0
font = pygame.font.SysFont(None, 36)

# Función para reiniciar el juego
def reset_game():
    global bird_y, obstacle_height, obstacle_x, score
    bird_y = height // 2
    obstacle_height = random.randint(100, height - 100)
    obstacle_x = width
    score = 0

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y -= 50

    # Aplicar gravedad al pájaro
    bird_y += gravity

    # Mover el obstáculo hacia la izquierda
    obstacle_x -= obstacle_speed

    # Verificar colisiones
    if bird_y > height or bird_y < 0:
        reset_game()

    if obstacle_x < 0:
        obstacle_x = width
        obstacle_height = random.randint(100, height - 100)
        score += 1

    if (
        bird_x < obstacle_x + obstacle_width
        and bird_x + bird_size > obstacle_x
        and (bird_y < obstacle_height or bird_y + bird_size > obstacle_height + space_between_obstacles)
    ):
        reset_game()

    # Limpiar la pantalla
    screen.fill(black)

    # Dibujar el pájaro
    pygame.draw.rect(screen, white, (bird_x, bird_y, bird_size, bird_size))

    # Dibujar el obstáculo
    pygame.draw.rect(screen, red, (obstacle_x, 0, obstacle_width, obstacle_height))
    pygame.draw.rect(screen, red, (obstacle_x, obstacle_height + space_between_obstacles, obstacle_width, height))

    # Dibujar la puntuación
    score_text = font.render(f"Puntuación: {score}", True, white)
    screen.blit(score_text, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(30)
