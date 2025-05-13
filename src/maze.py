from graphics import Point, Cell, Graphical_Item
import random

class Maze(Graphical_Item):
    def __init__(self, point_1, num_rows, num_cols, cell_size_x, cell_size_y, seed = None):
        self.__start_point = point_1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.cell_collection = [[] for x in range(self.__num_rows)]
        if seed is not None:
            random.seed(seed)
        self.Create_cells()

    def Create_cells(self):
        for x in range(self.__num_rows):
            for y in range(self.__num_cols):
                upper_left = Point(self.__start_point.x + x * self.__cell_size_x, self.__start_point.y + y * self.__cell_size_y)
                lower_right = Point(self.__start_point.x + (x + 1) * self.__cell_size_x, self.__start_point.y + (y + 1) * self.__cell_size_y)
                self.cell_collection[x].append(Cell(upper_left, lower_right))

    def Draw(self, canvas, fill_color):
        for x in range(self.__num_rows):
            for y in range(self.__num_cols):
                self.cell_collection[x][y].Draw(canvas, fill_color)

    def Draw_over_time(self, canvas, fill_color):
        for x in range(self.__num_rows):
            for y in range(self.__num_cols):
                yield self.cell_collection[x][y].Draw(canvas, fill_color)

    def Create_entry_and_exit(self):
        self.cell_collection[0][0].has_top_wall = False
        self.cell_collection[self.__num_rows - 1][self.__num_cols - 1].has_bottom_wall = False

    def Break_Walls_r(self, x, y):
        self.cell_collection[x][y].visited = True
        while True:
            to_visit = []
            if x - 1 >= 0:
                if not self.cell_collection[x - 1][y].visited:
                    to_visit.append((x - 1, y))
            if x + 1 < self.__num_rows:
                if not self.cell_collection[x + 1][y].visited:
                    to_visit.append((x + 1, y))
            if y - 1 >= 0:
                if not self.cell_collection[x][y - 1].visited:
                    to_visit.append((x, y - 1))
            if y + 1 < self.__num_cols:
                if not self.cell_collection[x][y + 1].visited:
                    to_visit.append((x, y + 1))
            if len(to_visit) <= 0:
                return
            else:
                chosen_dir = to_visit[random.randrange(0, len(to_visit))]
                if chosen_dir[0] < x:
                    self.cell_collection[x][y].has_left_wall = False
                    self.cell_collection[chosen_dir[0]][chosen_dir[1]].has_right_wall = False
                elif chosen_dir[0] > x:
                    self.cell_collection[x][y].has_right_wall = False
                    self.cell_collection[chosen_dir[0]][chosen_dir[1]].has_left_wall = False
                elif chosen_dir[1] < y:
                    self.cell_collection[x][y].has_top_wall = False
                    self.cell_collection[chosen_dir[0]][chosen_dir[1]].has_bottom_wall = False
                elif chosen_dir[1] > y:
                    self.cell_collection[x][y].has_bottom_wall = False
                    self.cell_collection[chosen_dir[0]][chosen_dir[1]].has_top_wall = False
                self.Break_Walls_r(chosen_dir[0], chosen_dir[1])

    def Reset_cells(self):
        for x in range(self.__num_rows):
            for y in range(self.__num_cols):
                self.cell_collection[x][y].visited = False

    def Solve(self):
        return self.Solve_r(0, 0)

    def Solve_r(self, x, y):
        self.cell_collection[x][y].visited = True
        if x == self.__num_rows - 1 and y == self.__num_cols - 1:
            return True
        
        if x - 1 >= 0 and not self.cell_collection[x][y].has_left_wall:
            if not self.cell_collection[x - 1][y].visited:
                pass

        if x + 1 < self.__num_rows and not self.cell_collection[x][y].has_right_wall:
            if not self.cell_collection[x + 1][y].visited:
                pass
        
        if y - 1 >= 0 and not self.cell_collection[x][y].has_top_wall:
            if not self.cell_collection[x][y - 1].visited:
                pass
        
        if y + 1 < self.__num_cols and not self.cell_collection[x][y].has_bottom_wall:
            if not self.cell_collection[x][y + 1].visited:
                pass