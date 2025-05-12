from window import Window
from graphics import Point, Cell
from maze import Maze

def main():
    win = Window(800, 600)
    start_point = Point(25, 25)
    maze = Maze(start_point, 15, 10, 50, 50)
    win.Draw_item(maze, "red")
    win.Wait_for_close()

main()