from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1: Point, point_2: Point):
        self.p1 = point_1
        self.p2 = point_2
    
    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, 
            self.p2.x, self.p2.y, 
            fill=fill_color, 
            width=2
        )

class Window: 
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Window")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running: 
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
        

class Cell:
    def __init__(self, win: Window,):
        self.left = True
        self.right = True
        self.top = True
        self.bottom = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, x2, y1, y2):
        if self.left:
            line = Line(Point(x1,y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.top:
            line = Line(Point(x1,y2), Point(x2, y2))
            self._win.draw_line(line)
        if self.right:
            line = Line(Point(x2,y2), Point(x2, y1))
            self._win.draw_line(line)
        if self.bottom:
            line = Line(Point(x2,y1), Point(x1, y1))
            self._win.draw_line(line)


