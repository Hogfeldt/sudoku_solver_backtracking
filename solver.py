import argparse

SIZE = 9

sudoku = [["0" for y in range(9)] for x in range(9)]


def parse_from_file(file_path):
    with open(file_path, "r") as fp:
        for i, line in enumerate(fp.readlines()):
            for j, value in enumerate(line.split()):
                if value != "0":
                    sudoku[i][j] = value


def sudoku_to_string():
    result = ""
    for row in sudoku:
        for value in row:
            result += " %s " % value
        result += "\n"
    return result


def check_for_valid_value(value, row, col):
    # Check for equal value in row
    for i in range(SIZE):
        if sudoku[i][col] == value:
            return False
    # Check for equal value in col
    for i in range(SIZE):
        if sudoku[row][i] == value:
            return False
    # Check for equal value in tile
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if sudoku[i][j] == value:
                return False
    return True


def find_unassigned_cell():
    for i, row in enumerate(sudoku):
        for j, value in enumerate(row):
            if value is "0":
                return (i, j)
    return None


def solve():
    unassigned = find_unassigned_cell()
    if unassigned == None:
        return True
    row, col = unassigned
    for i in range(1, 10):
        if check_for_valid_value(i, row, col):
            sudoku[row][col] = i
            if solve():
                return True
            sudoku[row][col] = "0"
    return False


def main():
    parser = argparse.ArgumentParser(
        description="Sudoku solver using a backtracking algorithm"
    )
    parser.add_argument("file_path", help="Path to file containing the sudoku")
    args = parser.parse_args()
    sudoku = parse_from_file(args.file_path)
    print(sudoku_to_string())
    if solve():
        print(sudoku_to_string())
    else:
        print("Unable to solve")


if __name__ == "__main__":
    main()
