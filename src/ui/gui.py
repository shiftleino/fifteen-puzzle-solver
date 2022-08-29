import pygame


class GraphicalUI:
    """The GraphicalUI-class is responsible for showing the optimal solution
    in an interactive window for the user.
    """
    def __init__(self):
        self._tile_size = 150
        self._font_size = 80
        self._display_color = (220, 220, 220)
        self._line_color = (100, 100, 100)

    def draw_grid(self, display):
        """Draws the grid of the board on the window.

        Args:
            display (pygame.display): The display where the grid is drawn.
        """
        for i in range(1, 4):
            pygame.draw.line(display, self._line_color, (i * self._tile_size, 0), (i * self._tile_size, 4 * self._tile_size), 10)
            pygame.draw.line(display, self._line_color, (0, i * self._tile_size), (4 * self._tile_size, i * self._tile_size), 10)

    def draw_tile_values(self, display, tile_values):
        """Draws the tile values of the board on the window.

        Args:
            display (pygame.display): The display where the tile values are drawn.
            tile_values ([][]int): The tile values of the board.
        """
        font = pygame.font.SysFont("arial", self._font_size)
        for i in range(4):
            pos_y = i * self._tile_size
            for j in range(4):
                pos_x = j * self._tile_size
                value = tile_values[i][j]
                if value < 10:
                    pos = (pos_x + 55, pos_y + 35)
                else:
                    pos = (pos_x + 30, pos_y + 35)
                if value == 16:
                    value = ""
                text = font.render(str(value), True, (0, 0, 0))
                display.blit(text, pos)

    def show_solution(self, solution_steps):
        """Draws every board of the solution path on the window, the user can see the next
        board by pressing space.

        Args:
            solution_steps ([][][]int): The boards in the optimal solution path.
        """
        pygame.init()
        display = pygame.display.set_mode((self._tile_size * 4, self._tile_size * 4))
        pygame.display.set_caption("15 Puzzle")
        display.fill(self._display_color)
        self.draw_grid(display)
        self.draw_tile_values(display, solution_steps[0])

        i = 1
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if i < len(solution_steps):
                            display.fill(self._display_color)
                            self.draw_grid(display)
                            self.draw_tile_values(display, solution_steps[i])
                            i += 1
                        else:
                            running = False

            pygame.display.update()

        pygame.quit()
