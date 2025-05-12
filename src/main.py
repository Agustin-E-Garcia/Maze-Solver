from window import Window
from graphics import Point, Line

def main():
    win = Window(800, 600)
    point_1 = Point(0, 0)
    point_2 = Point(800, 600)
    win.Draw_line(Line(point_1, point_2), "red")
    win.Wait_for_close()

main()