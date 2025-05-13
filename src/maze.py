from graphics import Point, Cell, Graphical_Item

class Maze(Graphical_Item):
    def __init__(self, point_1, num_rows, num_cols, cell_size_x, cell_size_y):
        self.__start_point = point_1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.cell_collection = [[] for x in range(self.__num_rows)]
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