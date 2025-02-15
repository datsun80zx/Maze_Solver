from window_class import Window, Point, Line, Cell
from maze_class import Maze


def main():
    win = Window(800, 800)
    maze = Maze(0, 0, 16, 16, 50, 50, win)
    x1 = maze._cells[0][0]._x1
    x2 = maze._cells[0][0]._x2
    y1 = maze._cells[0][0]._y1
    y2 = maze._cells[0][0]._y2

    print(f"first point is: ({x1, y1})\nsecond point is: ({x2, y2})")

    win.wait_for_close()

if __name__ == "__main__":
    main()
