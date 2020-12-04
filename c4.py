import random


def win_color(s):
    return "\x1b[6;30;42m" + s + "\x1b[0m"


def lose_color(s):
    return "\x1b[6;30;41m" + s + "\x1b[0m"


class C4(object):
    def __init__(self):
        self.n_rows = 6
        self.n_columns = 7
        self.no_token_label = "-"
        self.n_to_win = 4
        self.ai_label = "B"
        self.player_label = "R"
        self.board = [
            [self.no_token_label for i in range(self.n_columns)]
            for j in range(self.n_rows)
        ]
        random.seed()

    def __str__(self):
        output = ""
        for i in range(len(self.board)):
            row = "|".join(self.board[i])
            output += row + "\n"
        output += " ".join([str(i) for i in range(self.n_columns)]) + "\n"
        return output

    def drop_token(self, column, token):
        i = self.n_rows - 1
        while i > 0 and self.board[i][column] != self.no_token_label:
            i -= 1
        self.board[i][column] = token

    def board_is_full(self):
        for i in range(self.n_rows):
            for j in range(self.n_columns):
                if self.board[i][j] == self.no_token_label:
                    return False
        return True

    def column_is_full(self, column):
        board_column = [self.board[i][column] for i in range(self.n_rows)]
        empty = [c for c in board_column if c == self.no_token_label]
        return len(empty) == 0

    def make_ai_move(self):
        while True:
            c = random.randint(0, self.n_columns - 1)
            if not self.column_is_full(c):
                self.drop_token(c, self.ai_label)
                return

    def player_has_vertical_win_in_column(self, c, label):
        i = 0
        while i <= self.n_rows - self.n_to_win:
            if self.board[i][c] != label:
                i += 1
            elif self.board[i][c] != self.board[i + 1][c]:
                i += 1
            elif self.board[i][c] != self.board[i + 2][c]:
                i += 2
            elif self.board[i][c] != self.board[i + 3][c]:
                i += 3
            else:
                return [
                    (i, c),
                    (i + 1, c),
                    (i + 2, c),
                    (i + 3, c),
                ]
        return None

    def player_has_horizontal_win_in_row(self, r, label):
        j = 0
        while j <= self.n_columns - self.n_to_win:
            if self.board[r][j] != label:
                j += 1
            elif self.board[r][j] != self.board[r][j + 1]:
                j += 1
            elif self.board[r][j] != self.board[r][j + 2]:
                j += 2
            elif self.board[r][j] != self.board[r][j + 3]:
                j += 3
            else:
                return [
                    (r, j),
                    (r, j + 1),
                    (r, j + 2),
                    (r, j + 3),
                ]
        return None

    # ---xxxx
    # --xxxxx
    # -xxxxxx
    # xxxxxx-
    # xxxxx--
    # xxxx---
    def player_has_uphill_diagonal_win(self, label):
        for i, j in [
            (3, 0),
            (4, 0),
            (5, 0),
            (5, 1),
            (5, 2),
            (5, 3),
        ]:
            while i >= self.n_to_win - 1 and j <= self.n_columns - self.n_to_win:
                if self.board[i][j] != label:
                    i -= 1
                    j += 1
                elif self.board[i][j] != self.board[i - 1][j + 1]:
                    i -= 1
                    j += 1
                elif self.board[i][j] != self.board[i - 2][j + 2]:
                    i -= 2
                    j += 2
                elif self.board[i][j] != self.board[i - 3][j + 3]:
                    i -= 3
                    j += 3
                else:
                    return [
                        (i, j),
                        (i - 1, j + 1),
                        (i - 2, j + 2),
                        (i - 3, j + 3),
                    ]
        return None

    # xxxx---
    # xxxxx--
    # xxxxxx-
    # -xxxxxx
    # --xxxxx
    # ---xxxx
    def player_has_downhill_diagonal_win(self, label):
        for i, j in [
            (0, 3),
            (0, 2),
            (0, 1),
            (0, 0),
            (1, 0),
            (2, 0),
        ]:
            while (
                i <= self.n_rows - self.n_to_win and j <= self.n_columns - self.n_to_win
            ):
                if self.board[i][j] != label:
                    i += 1
                    j += 1
                elif self.board[i][j] != self.board[i + 1][j + 1]:
                    i += 1
                    j += 1
                elif self.board[i][j] != self.board[i + 2][j + 2]:
                    i += 2
                    j += 2
                elif self.board[i][j] != self.board[i + 3][j + 3]:
                    i += 3
                    j += 3
                else:
                    return [
                        (i, j),
                        (i + 1, j + 1),
                        (i + 2, j + 2),
                        (i + 3, j + 3),
                    ]
        return None

    def player_wins(self, label):
        for c in range(self.n_columns):
            cells = self.player_has_vertical_win_in_column(c, label)
            if cells is not None:
                return cells

        for r in range(self.n_rows)[-1::-1]:
            cells = self.player_has_horizontal_win_in_row(r, label)
            if cells is not None:
                return cells

        cells = self.player_has_uphill_diagonal_win(label)
        if cells is not None:
            return cells

        cells = self.player_has_downhill_diagonal_win(label)
        if cells is not None:
            return cells

        return None


def main():
    c4 = C4()
    print(f"You are {c4.player_label}, AI is {c4.ai_label}")
    while True:
        print(c4)
        try:
            while True:
                try:
                    column = int(input(f"Enter column (0 - {c4.n_columns - 1}): "))
                    assert 0 <= column < c4.n_columns
                    break
                except KeyboardInterrupt:
                    raise
                except Exception:
                    pass
        except KeyboardInterrupt:
            print("\nExiting")
            break

        c4.drop_token(column, c4.player_label)
        cells = c4.player_wins(c4.player_label)
        if cells is not None:
            for i, j in cells:
                c4.board[i][j] = win_color(c4.board[i][j])
            print(c4)
            print("You win!")
            break

        c4.make_ai_move()
        cells = c4.player_wins(c4.ai_label)
        if cells is not None:
            for i, j in cells:
                c4.board[i][j] = lose_color(c4.board[i][j])
            print(c4)
            print("AI wins!")
            break

        if c4.board_is_full():
            print("Draw")
            break


if __name__ == "__main__":
    main()
