from window_class import Window, Point, Line, Cell
from maze_class import Maze


def main():
    win = Window(800, 800)
    cell_size = 50
    num_rows = 800 // cell_size
    num_cols = 800 // cell_size
    maze = Maze(10, 10, num_rows, num_cols, 50, 50, win)
    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()
