from window_class import Window, Point, Line


def main():
    win = Window(800, 600)
    pt1 = Point(2,3)
    pt2 = Point(360,600)
    line1 = Line(pt1, pt2)

    win.draw_line(line1, "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()
