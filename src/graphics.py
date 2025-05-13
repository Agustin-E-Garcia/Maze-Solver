class Graphical_Item:
    def Draw(self, canvas, fill_color):
        pass

    def Draw_over_time(self, canvas, fill_color):
        self.Draw(canvas, fill_color)
        yield

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Line(Graphical_Item):
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def Draw(self, canvas, fill_color):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2)

class Cell(Graphical_Item):
    def __init__(self, upper_left_corner, lower_right_corner, left_wall = True, right_wall = True, top_wall = True, bottom_wall = True):
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self.visited = False
        
        middle_x = ((lower_right_corner.x - upper_left_corner.x) / 2) + upper_left_corner.x
        middle_y = ((lower_right_corner.y - upper_left_corner.y) / 2) + upper_left_corner.y
        self.middle_point = Point(middle_x, middle_y)

        self.left_wall = Line(upper_left_corner, Point(upper_left_corner.x, lower_right_corner.y))
        self.right_wall = Line(Point(lower_right_corner.x, upper_left_corner.y), lower_right_corner)
        self.top_wall = Line(upper_left_corner, Point(lower_right_corner.x, upper_left_corner.y))
        self.bottom_wall = Line(Point(upper_left_corner.x, lower_right_corner.y), lower_right_corner)

    def Draw(self, canvas, fill_color):
        if self.has_left_wall:
            self.left_wall.Draw(canvas, fill_color)
        else:
            self.left_wall.Draw(canvas, "grey")

        if self.has_right_wall:
            self.right_wall.Draw(canvas, fill_color)
        else:
            self.right_wall.Draw(canvas, "grey")
        
        if self.has_top_wall:
            self.top_wall.Draw(canvas, fill_color)
        else:
            self.top_wall.Draw(canvas, "grey")
        
        if self.has_bottom_wall:
            self.bottom_wall.Draw(canvas, fill_color)
        else:
            self.bottom_wall.Draw(canvas, "grey")

    def Draw_path(self, canvas, to_cell, undo=False):
        path = Line(self.middle_point, to_cell.middle_point)
        if undo:
            path.Draw(canvas, "red")
        else:
            path.Draw(canvas, "green")

class Path(Graphical_Item):
    def __init__(self):
        self.moves = []

    def Register_move(self, from_cell, to_cell, undo=False):
        self.moves.append((from_cell.middle_point, to_cell.middle_point, undo))

    def Draw_over_time(self, canvas, fill_color):
        for move in self.moves:
            line = Line(move[0], move[1])
            if move[2]:
                yield line.Draw(canvas, "red")
            else:
                yield line.Draw(canvas, "green")
