from window_class import Window, Point, Line, Cell
from maze_class import Maze


def main():
    win = Window(800, 800)
    maze = Maze(0, 0, 16, 16, 50, 50, win)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
