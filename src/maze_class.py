from window_class import *
import random
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
            seed=None,
    ):
        if seed != None: 
            random.seed(seed)

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._seed = seed
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

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
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        i = 0
        i2 = self._num_cols - 1
        j = 0
        j2 = self._num_rows - 1
        self._cells[i][j].top = False
        self._draw_cell(i, j)
        self._cells[i2][j2].bottom = False
        self._draw_cell(i2, j2)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = self._find_adj_cells(i, j)


        # now I need to pick a random direction from the to_visit list and recursively call the function
            if to_visit:
                dest = random.choice(to_visit)
                direction = list(dest.keys())[0]
                cell = dest[direction]
                opp_direction = {
                    "top": "bottom",
                    "bottom": "top",
                    "left": "right",
                    "right": "left",
                }
                setattr(self._cells[i][j], direction, False)
                setattr(self._cells[cell[0]][cell[1]], opp_direction[direction], False)
                self._break_walls_r(cell[0], cell[1])
            else:
                self._draw_cell(i, j)
                return

    def _find_adj_cells(self, i, j):
        to_visit = []
        left = i - 1
        right = i + 1
        up = j - 1
        down = j + 1

    # this block of code basically adds all of the adjacent cells to the list 
        # check if the cell to the left exists and has not been visited
        if i > 0 and self._cells[left][j].visited == False:
            to_visit.append({"left": (left, j)})
        # check if the cell to the right exists and has not been visited 
        if i < self._num_cols - 1 and self._cells[right][j].visited == False:
            to_visit.append({"right": (right, j)})
        
        # check if the cell above exists and has not been visited 
        if j > 0 and self._cells[i][up].visited == False:
            to_visit.append({"top": (i, up)})
        # check if the cell below exists and has not been visited
        if j < self._num_rows - 1 and self._cells[i][down].visited == False:
            to_visit.append({"bottom": (i, down)}) 

        return to_visit      

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        i = 0
        j = 0
        return self._solve_r(i, j)
    
    def _solve_r(self, i, j):
        end_i = self._num_cols - 1
        end_j = self._num_rows - 1

        self._animate()
        current = self._cells[i][j]
        current.visited = True
        adj_cells = self._find_adj_cells(i, j)
        if current == self._cells[end_i][end_j]:
            return True
        else:
            for item in adj_cells: 
                direction = list(item.keys())[0]
                cell = item[direction]
                if not getattr(self._cells[i][j], direction) and not self._cells[cell[0]][cell[1]].visited:
                    self._cells[i][j].draw_move(self._cells[cell[0]][cell[1]])
                    if self._solve_r(cell[0], cell[1]):
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[cell[0]][cell[1]], True)
