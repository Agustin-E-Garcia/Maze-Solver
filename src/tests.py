import unittest
import random
from maze import Maze
from graphics import Point

class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1.cell_collection), num_rows)
        self.assertEqual(len(m1.cell_collection[0]), num_cols)

    def test_maze_entry_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        m1.Create_entry_and_exit()
        self.assertEqual(m1.cell_collection[0][0].has_top_wall, False)
        self.assertEqual(m1.cell_collection[0][0].has_bottom_wall, True)
        self.assertEqual(m1.cell_collection[num_rows - 1][num_cols - 1].has_top_wall, True)
        self.assertEqual(m1.cell_collection[num_rows - 1][num_cols - 1].has_bottom_wall, False)

    def test_maze_reset_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        m1.Create_entry_and_exit()
        m1.Break_Walls_r(0, 0)
        m1.Reset_cells()
        self.assertEqual(m1.cell_collection[0][0].visited, False)
        self.assertEqual(m1.cell_collection[random.randrange(0, num_rows)][random.randrange(0, num_cols)].visited, False)
        

if __name__ == "__main__":
    unittest.main()