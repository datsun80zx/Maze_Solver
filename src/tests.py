import unittest
from maze_class import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_visit_reset(self):
        num_cols = 16
        num_rows = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 3)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(
                    m1._cells[i][j].visited,
                    False,
                    "this should show that all the cells have been reset",
                )
        

if __name__ == "__main__":
    unittest.main()
