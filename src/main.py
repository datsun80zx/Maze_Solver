from window_class import Window, Point, Line, Cell


def main():
    win = Window(800, 600)
    x1 = 250
    x2 = 500
    y1 = 250
    y2 = 500
    
    
    cell1 = Cell(win)
    cell1.right = False
    cell1.draw(x1, x2, y1, y2)

    # win.draw_line(line1, "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()
