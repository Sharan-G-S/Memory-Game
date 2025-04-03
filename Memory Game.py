import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Puzzle Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)

# Generate numbers for the game
grid_size = 4
numbers = list(range(1, 9)) * 2  # Create pairs of numbers
random.shuffle(numbers)
numbers = [numbers[i * grid_size:(i + 1) * grid_size] for i in range(grid_size)]

cell_size = WIDTH // grid_size

def draw_board(revealed):
    screen.fill(WHITE)
    for row in range(grid_size):
        for col in range(grid_size):
            x, y = col * cell_size, row * cell_size
            pygame.draw.rect(screen, GRAY, (x, y, cell_size, cell_size), 2)  # Grid border
            if revealed[row][col]:
                pygame.draw.rect(screen, GREEN, (x, y, cell_size, cell_size))
                font = pygame.font.Font(None, 50)
                text = font.render(str(numbers[row][col]), True, BLACK)
                screen.blit(text, (x + cell_size//3, y + cell_size//3))
            else:
                pygame.draw.rect(screen, BLUE, (x, y, cell_size, cell_size))
    pygame.display.flip()

def main():
    revealed = [[False] * grid_size for _ in range(grid_size)]
    first_pick = None
    running = True

    while running:
        draw_board(revealed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                col, row = x // cell_size, y // cell_size
                
                if not revealed[row][col]:
                    revealed[row][col] = True
                    draw_board(revealed)
                    
                    if first_pick is None:
                        first_pick = (row, col)
                    else:
                        r1, c1 = first_pick
                        if numbers[r1][c1] != numbers[row][col]:
                            time.sleep(0.5)
                            revealed[r1][c1] = False
                            revealed[row][col] = False
                        first_pick = None
        
    pygame.quit()

if __name__ == "__main__":
    main()
