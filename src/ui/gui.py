import pygame

TILE_SIZE = 150
FONT_SIZE = 80
DISPLAY_COLOR = (220, 220, 220)
LINE_COLOR = (100, 100, 100)


def draw_grid(display):
    for i in range(1, 4):
        pygame.draw.line(display, LINE_COLOR, (i * TILE_SIZE, 0), (i * TILE_SIZE, 4 * TILE_SIZE), 10)
        pygame.draw.line(display, LINE_COLOR, (0, i * TILE_SIZE), (4 * TILE_SIZE, i * TILE_SIZE), 10)

def draw_tile_values(display, tile_values):
    font = pygame.font.SysFont("arial", FONT_SIZE)
    for i in range(4):
        pos_y = i * TILE_SIZE
        for j in range(4):
            pos_x = j * TILE_SIZE
            value = tile_values[i][j]
            if value < 10:
                pos = (pos_x + 55, pos_y + 35)
            else:
                pos = (pos_x + 30, pos_y + 35)
            if value == 16:
                value = ""
            text = font.render(str(value), True, (0, 0, 0))
            display.blit(text, pos)

def show_solution(solution_steps):
    pygame.init()
    display = pygame.display.set_mode((TILE_SIZE * 4, TILE_SIZE * 4))
    pygame.display.set_caption("15 Puzzle")
    display.fill(DISPLAY_COLOR)
    draw_grid(display)
    draw_tile_values(display, solution_steps[0])

    i = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if i < len(solution_steps):
                        display.fill(DISPLAY_COLOR)
                        draw_grid(display)
                        draw_tile_values(display, solution_steps[i])
                        i += 1

        pygame.display.update()

    pygame.quit()
