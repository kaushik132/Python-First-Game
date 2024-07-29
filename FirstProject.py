import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racing Game")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the car
car_width, car_height = 50, 100
car = pygame.image.load('car2.png')
car = pygame.transform.scale(car, (car_width, car_height))
car_x, car_y = width // 2 - car_width // 2, height - car_height - 20

# Set up the tree obstacle
tree_width, tree_height = 50, 100
tree = pygame.image.load('man.png')
tree = pygame.transform.scale(tree, (tree_width, tree_height))
obstacle_x, obstacle_y = random.randint(0, width - tree_width), -tree_height
obstacle_speed = 7

# Set up the score
score = 0
font = pygame.font.SysFont(None, 55)

def draw_car(x, y):
    window.blit(car, (x, y))

def draw_tree(x, y):
    window.blit(tree, (x, y))

def draw_score(score):
    score_text = font.render("Score: " + str(score), True, black)
    window.blit(score_text, (10, 10))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= 10
    if keys[pygame.K_RIGHT] and car_x < width - car_width:
        car_x += 10

    obstacle_y += obstacle_speed

    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, tree_width, tree_height)
    
    if car_rect.colliderect(obstacle_rect):
        score += 1
        obstacle_x, obstacle_y = random.randint(0, width - tree_width), -tree_height

    if obstacle_y > height:
        print(f"Game Over! Final Score: {score}")
        pygame.quit()
        exit()

    window.fill(white)
    draw_car(car_x, car_y)
    draw_tree(obstacle_x, obstacle_y)
    draw_score(score)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
