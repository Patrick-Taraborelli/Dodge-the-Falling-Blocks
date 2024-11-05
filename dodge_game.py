import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 10

# Enemy settings
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 5

# Game settings
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Game functions
def detect_collision(player_pos, enemy_pos):
    px, py = player_pos
    ex, ey = enemy_pos
    if (px < ex + enemy_size and px + player_size > ex) and (py < ey + enemy_size and py + player_size > ey):
        return True
    return False

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Enemy movement
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        enemy_speed += 0.5  # Increase difficulty as score increases

    # Check for collision
    if detect_collision(player_pos, enemy_pos):
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    # Draw player and enemy
    pygame.draw.rect(screen, BLUE, (*player_pos, player_size, player_size))
    pygame.draw.rect(screen, RED, (*enemy_pos, enemy_size, enemy_size))

    # Display score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display and set frame rate
    pygame.display.flip()
    clock.tick(30)
