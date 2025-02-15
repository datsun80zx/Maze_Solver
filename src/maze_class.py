from window_class import *
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()


    def _create_cells(self):
        # for a 8 columns & rows you need 9 x and y values, 
        # to draw a column you are only increasing the y values x values stay the same
        # so basically you would determine the size of the cell and then increase the y values by that amount
        # size of the cell would be determined by dividing the window variables evenly by the number of cols and rows. 
        for i in range(self._num_cols):
            rows = []
            for j in range(self._num_rows):
                rows.append(Cell(self._win))
            self._cells.append(rows)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        


    def _draw_cell(self, i, j):
        x1 = self._x1 + (self._cell_size_x * i)
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + (self._cell_size_y * j)
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, x2, y1, y2)
        self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.0)

    def _break_entrance_and_exit(self):
        i = 0
        i2 = self._num_cols - 1
        j = 0
        j2 = self._num_rows - 1
        self._cells[i][j].top = False
        self._draw_cell(i, j)
        self._cells[i2][j2].bottom = False
        self._draw_cell(i2, j2)
