from graphics import Window,Point, Line, Cell
import time
import random
random.seed(1)

class Maze:
    def __init__(self, x1, y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win = None):
        self._win = win
        self.x1 = x1
        self.y1 = y1
        self._num_rows = num_rows       
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        

    def _create_cells(self):
        if self._win is None:
            return
        
        
        for i in range(self._num_cols):
            col_cells = []
            self._cells.append(col_cells)
            for j in range(self._num_rows):
                cell = Cell(self._win)
                col_cells.append(cell)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
                self._animate()
                

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self.x1 + i * self._cell_size_x
        y1 = self.y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
        
    def _break_entrance_and_exit(self):
        if self._win is None:
            return
        entrance_cell =self._cells[0][0]
        entrance_cell.has_top_wall =False
        self._draw_cell(0, 0)
        exit_cell = self._cells[self._num_cols-1][self._num_rows-1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def possible_directions(self, i, j):
        possible_directions = []
        if j > 0 and self._cells[i][j-1].visited == False:
            possible_directions.append(self._cells[i][j-1])
        if j < self._num_rows - 1 and self._cells[i][j+1].visited == False:
            possible_directions.append(self._cells[i][j+1])
        if i > 0 and self._cells[i-1][j].visited == False:
            possible_directions.append(self._cells[i-1][j])
        if i < self._num_cols - 1 and self._cells[i+1][j].visited == False:
            possible_directions.append(self._cells[i+1][j])
        return possible_directions
    
    
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            possible_directions = self.possible_directions(i, j)
            if len(possible_directions) == 0:
                return
            next_cell = random.choice(possible_directions)
            if  j > 0 and next_cell == self._cells[i][j-1] :
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i, j-1)
                self._break_walls_r(i, j-1)
            elif j < self._num_rows - 1 and next_cell == self._cells[i][j+1]:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i, j+1)
                self._break_walls_r(i, j+1)
            elif i > 0 and next_cell == self._cells[i-1][j]:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i-1, j)
                self._break_walls_r(i-1, j)
            elif i < self._num_cols - 1 and next_cell == self._cells[i+1][j]:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i+1, j)
                self._break_walls_r(i+1, j)            
            

            



        
                        
        


                

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    

    


        

    

    
        



        

   