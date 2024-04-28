import numpy as np


class GameField:
    FILE_SPLITTER = ";"
    S_EMPTY = "0"
    MOVE_MAX_COUNT = 200
    FIELD_SIZE = 32  # Assuming the field is always 32x32

    class Cell:
        EMPTY = 0
        APPLE = 1

    class Direction:
        RIGHT = [0, 1]
        DOWN = [1, 0]
        LEFT = [0, -1]
        UP = [-1, 0]

        def __init__(self, dx, dy):
            self.move = [dx, dy]

        def get_move(self):
            return self.move

    def __init__(self):
        self.init_field = np.zeros((self.FIELD_SIZE, self.FIELD_SIZE), dtype=int)

    def fill(self, filename):
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file):
                self.fill_line(line_num, line.strip())

    def fill_line(self, line_num, line):
        cells = line.split(self.FILE_SPLITTER)
        for i, cell in enumerate(cells):
            self.init_field[line_num, i] = self.Cell.EMPTY if cell == self.S_EMPTY else self.Cell.APPLE

    def testAnt(self, chromosome):
        from Ant import Ant  # Assuming Ant class has been defined and is in ant.py
        ant = Ant(chromosome)
        field = np.copy(self.init_field)
        eaten_apple_count = 0
        ant_direction = self.Direction.RIGHT
        ant_pos = [0, 0]

        for _ in range(self.MOVE_MAX_COUNT):
            forward_pos = self.get_forward_cell_coord(ant_pos, ant_direction, self.FIELD_SIZE)
            forward_cell = field[forward_pos[0], forward_pos[1]]
            ant_action = ant.getAction(forward_cell)

            if ant_action == Ant.Action.MOVE_FORWARD:
                ant_pos = forward_pos
                if field[ant_pos[0], ant_pos[1]] == self.Cell.APPLE:
                    field[ant_pos[0], ant_pos[1]] = self.Cell.EMPTY
                    eaten_apple_count += 1

            ant_direction = self.get_new_direction(ant_direction, ant_action)

        return eaten_apple_count

    def get_forward_cell_coord(self, cur_pos, direction, field_size):
        move = direction.get_move()
        new_pos = [cur_pos[0] + move[0], cur_pos[1] + move[1]]
        new_pos = [n % field_size for n in new_pos]  # Wrap around for toroidal field
        return new_pos

    def get_new_direction(self, old_direction, action):
        from Ant import Ant
        if action == Ant.Action.TURN_LEFT:
            return self.Direction.LEFT if old_direction == self.Direction.UP else \
                   self.Direction.DOWN if old_direction == self.Direction.LEFT else \
                   self.Direction.RIGHT if old_direction == self.Direction.DOWN else \
                   self.Direction.UP
        elif action == Ant.Action.TURN_RIGHT:
            return self.Direction.RIGHT if old_direction == self.Direction.UP else \
                   self.Direction.UP if old_direction == self.Direction.LEFT else \
                   self.Direction.LEFT if old_direction == self.Direction.DOWN else \
                   self.Direction.DOWN
        return old_direction
