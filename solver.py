import argparse

_tile_coords = [
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
    [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
    [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
    [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
    [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
    [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
    [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
    [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
    [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
]


class Sudoku:
    def __init__(self, file_path):
        self.cells = [[None for y in range(9)] for x in range(9)]
        with open(file_path, "r") as fp:
            for i, line in enumerate(fp.readlines()):
                for j, value in enumerate(line.split()):
                    if value != "x":
                        self.cells[i][j] = value

    def get_cell(self, row, column):
        return self.cell[row][column]

    def set_cell(self, row, column, value):
        self.cells[row][column] = value

    def get_corresponding_tile_coords(self, row, column):
        result = []
        for tile in _tile_coords:
            if (row, column) in tile:
                return tile
        return None

    def __str__(self):
        result = ""
        for r in self.cells:
            for c in r:
                if c != None:
                    result += " %s " % c
                else:
                    result += " x "
            result += "\n"
        return result


def solve(file_path):
    sudoku = Sudoku(file_path)
    print(sudoku.get_corresponding_tile_coords(1, 2))


def main():
    parser = argparse.ArgumentParser(
        description="Sudoku solver using a backtracking algorithm"
    )
    parser.add_argument("file_path", help="Path to file containing the sudoku")
    args = parser.parse_args()
    solve(args.file_path)


if __name__ == "__main__":
    main()
