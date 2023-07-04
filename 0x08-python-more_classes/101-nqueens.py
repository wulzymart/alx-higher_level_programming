#!/usr/bin/python3
import sys


def is_valid_state(state, n):
    """check if it is a valid solution"""
    return len(state) == n


def get_candidates(state, n):
    """Gets posible candidates to position queen"""
    if not state:
        return range(n)
    # find next position
    position = len(state)
    candidates = set(range(n))
    # prune down candidates that place the queen into atacks
    for row, col in enumerate(state):
        # discard column with queen
        candidates.discard(col)
        dist = position - row
        # discard diagonals
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    return candidates


def search(state, solutions, n):
    """Searches all positions to see the valid states"""
    if is_valid_state(state, n):
        result = []
        for row, col in enumerate(state):
            result.append([row, col])
        solutions.append(result.copy())
        return

    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.remove(candidate)


def solve_N_Queen(n):
    """Main solution function

    Args:
        n (int): size of chess board
    """
    solutions = []
    state = []
    search(state, solutions, n)
    return solutions


def print_N_queen(n):
    """Prints solution of n size"""
    solution = solve_N_Queen(n)
    for i in solution:
        print(i)


# Main program
if __name__ == '__main__':
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
    print_N_queen(n)
