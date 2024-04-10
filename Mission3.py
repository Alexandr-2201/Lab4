import time

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_queens(board, row):
    n = len(board)
    if row == n:
        print_solution(board)
        return True

    found_solution = False
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            found_solution = solve_queens(board, row + 1) or found_solution
            board[row] = -1

    return found_solution

def print_solution(board):
    n = len(board)
    for i in range(n):
        row_str = ""
        for j in range(n):
            if board[i] == j:
                row_str += "Q "
            else:
                row_str += ". "
        print(row_str)
    print()

n = 8
board = [-1] * n

start_time = time.time()
if not solve_queens(board, 0):
    print("Решение не найдено.")
print("--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
