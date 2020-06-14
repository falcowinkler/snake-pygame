import random


class Game:

    def __init__(self, board_size):
        self.board_size = board_size
        self.snake = [(0, 0)]
        self.place_food()
        self.direction = (1, 0)
        self.score = 0
        self.crashed = False

    def random_coordinate(self):
        return random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)

    def place_food(self):
        x, y = self.random_coordinate()
        while (x, y) in self.snake:
            x, y = self.random_coordinate()
        self.food = x, y

    def step(self):
        dx, dy = self.direction
        head_x, head_y = self.snake[0]
        new_x, new_y = (head_x + dx) % self.board_size, (head_y + dy) % self.board_size
        if (new_x, new_y) in self.snake:
            self.crashed = True
        elif self.food == (new_x, new_y):
            self.place_food()
            self.score += 1
        else:
            self.snake.pop()
        self.snake.insert(0, (new_x, new_y))

    def change_dir(self, direction):
        new_dx, new_dy = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}[direction]
        dx, dy = self.direction
        if (dx + new_dx, dy + new_dy) != (0, 0):
            self.direction = (new_dx, new_dy)

    def game_over(self):
        return self.crashed
