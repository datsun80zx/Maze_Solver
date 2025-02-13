from window_class import Window, Point, Line, Cell


def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.right = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.left = False
    c2.bottom = False
    c2.draw(100, 50, 150, 100)

    c1.draw_move(c2)

    c3 = Cell(win)
    c3.top = False
    c3.right = False
    c3.draw(100, 100, 150, 150)

    c2.draw_move(c3)

    c4 = Cell(win)
    c4.left = False
    c4.draw(150, 100, 200, 150)

    c3.draw_move(c4, True)
    win.wait_for_close()

if __name__ == "__main__":
    main()
