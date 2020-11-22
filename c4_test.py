import unittest

from c4 import C4


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


if __name__ == "__main__":
    unittest.main()
