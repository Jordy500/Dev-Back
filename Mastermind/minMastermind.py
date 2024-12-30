"""
This script implements a simple Mastermind game using Pygame. The player has to guess a secret code consisting of 4 digits (0-9) within a limited number of attempts. The game provides hints after each guess indicating how many digits are correctly placed and how many are correct but misplaced.
Functions:
- generate_hint(secret, guess): Generates a hint based on the player's guess compared to the secret code.
- draw(): Renders the game screen, including the player's guesses, buttons, and hints.
Game Variables:
- secret_code: The randomly generated secret code.
- player_input: The current input from the player.
- max_attempts: The maximum number of attempts allowed.
- active_cell: The currently active cell for input.
- attempts: A list of all the player's guesses and corresponding hints.
- game_over: A flag indicating whether the game is over.
- hint_message: A message providing feedback to the player.
Pygame Elements:
- screen: The game window.
- buttons: Rectangles representing the number buttons for input.
- colors: Predefined colors used in the game.
- fonts: Predefined fonts used for rendering text.
"""
import random
import pygame
import sys

pygame.init()

screen_width, screen_height = 900, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Welcome to the Mastermind game!")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
HIGHLIGHT = (255, 204, 0)

# fonts
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 35)

# game variables
secret_code = [random.randint(0, 9) for _ in range(4)]
player_input = ["_", "_", "_", "_"]
max_attempts = 5
active_cell = 0
attempts = []
max_attempts = 10
game_over = False
hint_message = ""
      
# bouton for choosing the number
buttons = [
    pygame.Rect(50 + i * 80, 700, 60, 50) for i in range(10)
]

def generate_hint(secret, guess):
    correct_position = sum(s == g for s, g in zip(secret, guess))
    correct_number = sum(min(secret.count(n), guess.count(n)) for n in set(guess)) - correct_position
    return f"{correct_position} bien placé(s), {correct_number} mal placé(s)"

def draw():
    screen.fill(WHITE)

    # draw guesses
    for i, guess in enumerate(attempts):
         y = 50 + i * 60
         for j, num in enumerate(guess["guess"]):
            pygame.draw.rect(screen, RED, (50 + j * 80, y, 60, 50))
            text = font.render(str(num), True, BLACK)
            screen.blit(text, (60 + j * 80, y + 5))
    

    y = 50 + len(attempts) * 60
    for j in range(4):
        color = HIGHLIGHT if j == active_cell else WHITE
        pygame.draw.rect(screen, color, (50 + j * 80, y, 60, 50))
        text = font.render(str(player_input[j]), True, BLACK)
        screen.blit(text, (60 + j * 80, y + 5))

    # draw buttons
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, WHITE, button)
        text = font.render(str(i), True, BLACK)
        screen.blit(text, (button.x + 15, button.y + 5))

    # Afficher les informations de l'indice
    if attempts:
        hint_text = small_font.render(attempts[-1]["hint"], True, GREEN)
        screen.blit(hint_text, (400, y + 10))

    if game_over:
        game_over_text = font.render("Game Over!", True, RED)
        screen.blit(game_over_text, (screen_width // 2 - 100, screen_height - 100))
        secret_text = small_font.render(f"Code secret : {''.join(map(str, secret_code))}", True, BLACK)
        screen.blit(secret_text, (screen_width // 2 - 100, screen_height - 60))

    pygame.display.flip()


running = True
while running:
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            for i, button in enumerate(buttons):
                if button.collidepoint(event.pos):
                    player_input[active_cell] = i
                    active_cell = (active_cell + 1) % 4
                    break

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game_over:
                if "_" in player_input:
                    hint_message = "Complétez votre ligne !"
                else:
                    guess = list(map(int, player_input))
                    hint = generate_hint(secret_code, guess)
                    attempts.append({"guess": player_input.copy(), "hint": hint})
                    player_input = ["_", "_", "_", "_"]
                    active_cell = 0

                    if guess == secret_code:
                        hint_message = "Félicitations, vous avez gagné !"
                        game_over = True
                    elif len(attempts) >= max_attempts:
                        game_over = True

pygame.quit()
sys.exit()



