#!/usr/bin/python3
"""Solves the N queens problem using backtracking
ensure that N non-attacking queens are placed on a nxn chessboard.

"""
import sys

def backtrack(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True
def solveNqueens(board, row, n):
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if backtrack(board, row, col):
            board[row] = col
            solveNqueens(board, row + 1, n)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

        try:
            n = int(sys.argv[1])
        except ValueError:
            print("N must be a number")
            sys.exit(1)

        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        board = [-1] * n
        solveNqueen(board, 0, n)

    if __name__ == "__main__":
        main()
