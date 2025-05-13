from window import Window
from graphics import Point, Cell
from maze import Maze
import time

def main():
    win = Window(800, 600)
    maze = Maze(Point(25, 25), 15, 10, 50, 50)

    finished_drawin_maze = False
    added_entry_and_exit = False
    
    maze_draw = win.Draw_item_over_time(maze, "red")
    
    while win.Is_active():
        if not finished_drawin_maze:    
            finished_drawin_maze = next(maze_draw, True)
        elif not added_entry_and_exit:
            maze.Create_entry_and_exit()
            win.Draw_item(maze, "red")

        
        win.Redraw()
        time.sleep(0.05)

main()