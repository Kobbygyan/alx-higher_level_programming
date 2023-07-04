#!/usr/bin/python3

import sys


def solve_nqueens(N):
    """
    Solve the N-Queens problem and print all possible solutions.

    Args:
        N (int): The number of queens and the size of the chessboard.
    """
    def is_safe(board, row, col):
        """
        Check if it's safe to place a queen at the given position.

        Args:
            board (list): The current state of the chessboard.
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        # Check the row
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        # Check the upper diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check the lower diagonal
        i, j = row, col
        while i < N and j >= 0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1

        return True

    def backtrack(board, col, solutions):
        """
        Backtracking function to find all solutions.

        Args:
            board (list): The current state of the chessboard.
            col (int): The column index.
            solutions (list): List to store the solutions.
        """
        if col == N:
            # Found a solution, add it to the list
            solutions.append([''.join(row) for row in board])
            return

        for row in range(N):
            if is_safe(board, row, col):
                # Place a queen at the current position
                board[row][col] = 'Q'
                backtrack(board, col + 1, solutions)
                # Remove the queen from the current position for backtracking
                board[row][col] = '.'

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    backtrack(board, 0, solutions)

    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
