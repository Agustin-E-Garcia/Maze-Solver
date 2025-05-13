import unittest
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

if __name__ == "__main__":
    unittest.main()