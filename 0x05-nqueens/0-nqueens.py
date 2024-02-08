#!/usr/bin/python3
""" N Queens """
from sys import argv, exit


def solve_n_queens(size):
    """Program that solves the N queens problem"""
    solutions = []
    queens = [-1] * size

    def dfs(index):
        """Recursively resolves the N queens problem"""
        if index == len(queens):
            solutions.append(queens[:])
            return
        for x in range(len(queens)):
            queens[index] = x
            if is_valid(index):
                dfs(index + 1)

    def is_valid(n):
        """Method that checks if a position in the board is valid"""
        for x in range(n):
            if abs(queens[x] - queens[n]) == n - x:
                return False
            if queens[x] == queens[n]:
                return False
        return True


    def create_main_boards(solutions):
        """Method that builds the List that will be returned"""
        main_boards = []
        for queens in solutions:
            board = []
            for row, col in enumerate(queens):
                board.append([row, col])
            main_boards.append(board)
        return main_boards

    dfs(0)
    return create_main_boards(solutions)


if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        size = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if size < 4:
        print('N must be at least 4')
        exit(1)
    else:
        result = solve_n_queens(size)
        for row in result:
            print(row)
