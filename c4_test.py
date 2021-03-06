import unittest

from c4 import C4, InvalidMoveError


class C4Test(unittest.TestCase):
    def test_vertical_wins(self):
        c4 = C4()
        c4.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
        self.assertIsNone(c4.player_wins(1))

        c4.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
        ]
        self.assertEqual(
            c4.player_wins(1),
            [(2, 6), (3, 6), (4, 6), (5, 6)],
        )

        c4.board = [
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 2, 0, 0, 2],
        ]
        self.assertEqual(
            c4.player_wins(1),
            [(1, 3), (2, 3), (3, 3), (4, 3)],
        )

    def test_horizontal_wins(self):
        c4 = C4()
        c4.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 2, 2, 2, 0, 0],
        ]
        self.assertIsNone(c4.player_wins(1))

        c4.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 2, 1, 2, 0],
            [0, 0, 1, 1, 1, 2, 0],
        ]
        self.assertEqual(
            c4.player_wins(1),
            [(3, 2), (3, 3), (3, 4), (3, 5)],
        )

    def test_diagonal_wins(self):
        c4 = C4()
        c4.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 0],
            [1, 2, 2, 2, 1, 1, 0],
            [2, 1, 1, 1, 2, 1, 1],
        ]
        self.assertEqual(
            c4.player_wins(2),
            [(5, 0), (4, 1), (3, 2), (2, 3)],
        )

        c4.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 2, 2, 2, 0],
            [0, 0, 2, 2, 1, 1, 0],
            [1, 1, 2, 2, 1, 1, 0],
            [1, 1, 2, 1, 2, 1, 1],
        ]
        self.assertEqual(
            c4.player_wins(2),
            [(4, 2), (3, 3), (2, 4), (1, 5)],
        )
        self.assertIsNone(c4.player_wins(1))

        c4.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 2, 2, 1, 0, 0],
            [0, 0, 1, 2, 2, 1, 0],
            [0, 0, 2, 2, 2, 1, 0],
        ]
        self.assertEqual(
            c4.player_wins(1),
            [(1, 2), (2, 3), (3, 4), (4, 5)],
        )
        self.assertIsNone(c4.player_wins(2))

    def test_column_is_full(self):
        c4 = C4()
        c4.board = [
            ["-", "-", "-", 2, "-", "-", "-"],
            ["-", "-", "-", 2, "-", "-", "-"],
            ["-", "-", "-", 2, "-", "-", "-"],
            ["-", "-", 2, 1, "-", "-", "-"],
            ["-", "-", 2, 1, "-", "-", "-"],
            ["-", "-", 1, 1, "-", "-", "-"],
        ]
        self.assertTrue(c4.column_is_full(3))
        self.assertFalse(c4.column_is_full(2))
        with self.assertRaises(InvalidMoveError):
            c4.drop_token(3, 1)

    def test_copy_from(self):
        c4 = C4()
        c4.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 2, 2, 1, 0, 0],
            [0, 0, 1, 2, 2, 1, 0],
            [0, 0, 2, 2, 2, 1, 0],
        ]
        c4_copy = C4().copy_from(c4)
        self.assertEqual(c4.board, c4_copy.board)


if __name__ == "__main__":
    unittest.main()
