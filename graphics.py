from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("mazr-solver")
        
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__root.protocol("MY_DELETE", self.close)
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        
    def close(self):
        self.__running = False

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color="black)"):
        canvas.create_line(self.start.x, self.start.y,
                            self.end.x, self.end.y,
                            fill=fill_color,
                            width=2)  
        
class Cell:
    def __init__(self,win,
                 has_left_wall=True,
                 has_top_wall=True,
                 has_right_wall=True,
                 has_bottom_wall=True):
        
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.visited = False
        
    
    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.has_left_wall:
            line =Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, fill_color="white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill_color="white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, fill_color="white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, fill_color="white")

    def draw_move(self, to_cell, undo=False):
        line = Line(Point((self.x1+self.x2) // 2, (self.y1+self.y2) // 2), 
                    Point((to_cell.x1+to_cell.x2) // 2, (to_cell.y1+to_cell.y2) // 2)   )
        if undo:
            self._win.draw_line(line, fill_color="grey")
        else:
            self._win.draw_line(line, fill_color="red")

