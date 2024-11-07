#!/usr/bin/python3
"""
N Queens puzzle solution
Places N non-attacking queens on an NxN chessboard
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if a queen can be placed on board[row][col]

    Args:
        board: 2D list representing the board
        row: row to check
        col: column to check
        N: size of the board

    Returns:
        Boolean indicating if the position is safe
    """
    # Check this row on left side
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solve the N queens puzzle and print all solutions

    Args:
        N: size of the board and number of queens
    """
    # Initialize empty board
    board = [[0 for x in range(N)] for y in range(N)]
    solutions = []
    solve_util(board, 0, N, solutions)

    # Print solutions in required format
    for sol in solutions:
        formatted = [[i, pos] for i, pos in enumerate(sol)]
        print(formatted)


def solve_util(board, col, N, solutions):
    """
    Utility function to solve N Queens problem using backtracking

    Args:
        board: 2D list representing the board
        col: current column
        N: size of the board
        solutions: list to store all solutions
    """
    if col >= N:
        # Convert board to solution format
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append(j)
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_util(board, col + 1, N, solutions)
            board[i][col] = 0


def main():
    """Main function to handle input and program flow"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
