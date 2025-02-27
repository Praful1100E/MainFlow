import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
X_COLOR = (0, 200, 255)
O_COLOR = (255, 100, 100)

# Screen dimensions
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
CELL_SIZE = WIDTH // BOARD_COLS

# Initialize board
board = [" " for _ in range(9)]  # 3x3 board stored as a list

# Create pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe AI")

# Fonts
font = pygame.font.Font(None, 100)

# Draw the grid
def draw_grid():
    screen.fill(WHITE)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)

# Draw X and O
def draw_marks():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            index = row * 3 + col
            if board[index] == "X":
                pygame.draw.line(screen, X_COLOR, (col * CELL_SIZE + 50, row * CELL_SIZE + 50),
                                 ((col + 1) * CELL_SIZE - 50, (row + 1) * CELL_SIZE - 50), LINE_WIDTH)
                pygame.draw.line(screen, X_COLOR, ((col + 1) * CELL_SIZE - 50, row * CELL_SIZE + 50),
                                 (col * CELL_SIZE + 50, (row + 1) * CELL_SIZE - 50), LINE_WIDTH)
            elif board[index] == "O":
                pygame.draw.circle(screen, O_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 3, LINE_WIDTH)

# Check for a winner
def check_winner(player):
    win_patterns = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_patterns)

# Minimax algorithm for AI
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    elif check_winner("X"):
        return -1
    elif " " not in board:
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI chooses the best move
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Display result message
def show_result(text):
    screen.fill(WHITE)
    result_text = font.render(text, True, BLACK)
    screen.blit(result_text, (WIDTH//4, HEIGHT//3))
    pygame.display.flip()
    pygame.time.delay(2000)

# Game loop
def main():
    running = True
    player_turn = True

    draw_grid()
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                x, y = event.pos
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                index = row * 3 + col

                if board[index] == " ":
                    board[index] = "X"
                    player_turn = False

                    if check_winner("X"):
                        draw_marks()
                        pygame.display.flip()
                        show_result("You Win! ")
                        return

                    if " " in board:
                        best_move()
                        if check_winner("O"):
                            draw_marks()
                            pygame.display.flip()
                            show_result("AI Wins! ")
                            return

                    if " " not in board:
                        draw_marks()
                        pygame.display.flip()
                        show_result("It's a Draw! ")
                        return

                draw_marks()
                pygame.display.flip()
                player_turn = True

# Run the game
main()