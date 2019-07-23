import argparse

def solve(file_path):
    print(file_path)

def main():
    parser = argparse.ArgumentParser(description="Sudoku solver using a backtracking algorithm")
    parser.add_argument("file_path", help="Path to file containing the sudoku")
    args = parser.parse_args()
    solve(args.file_path)
    
if __name__=='__main__':
    main()
