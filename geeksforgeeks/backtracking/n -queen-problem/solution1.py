def main():
    test_case = int(input())
    for _ in range(test_case):
        n = int(input())
        print_solution(n)


def print_solution(n):
    board = []
    
    for row in range(n):
        cols = ['' for _ in range(n)]
        board.append(cols)

    solutions = get_all_solutions(board, n)
    if len(solutions) == 0:
        print(-1)
    else:
        for solution in solutions:
            print("[", end="")
            for item in solution:
                print(item, end=" ")
            print("]", end=" ")
        print("")


def get_all_solutions(board, n):
    occupied_rows = set()    
    result = []
    answer = []

    for solution in try_find_solution(board, 0, n, occupied_rows, answer):
        result.append(solution.copy())

    return result


def try_find_solution(board: list, col: int, n: int, occupied_rows: set, solution: list):    
    for row in range(n):
        if (not row in occupied_rows) and diagonal_is_safe(board, n, row, col):
            board[row][col] = 'q'
            solution.append(row + 1) # in answers row starts from 1
            occupied_rows.add(row)

            if col+1 < n:                
                yield from try_find_solution(board, col+1, n, occupied_rows, solution)
            elif col == n-1 and len(solution) == n:
                yield solution            
            
            board[row][col] = ''
            solution.pop()
            occupied_rows.remove(row)


def diagonal_is_safe(board, n, row, col):
    for r, c in get_diagonal_cells(row, col, n):
        if board[r][c] != '':
            return False

    return True


def get_diagonal_cells(row, col, n):
    r = row
    c = col
    # direction up-right
    while r != 0 and c != n-1:
        r = r - 1
        c = c + 1
        yield r,c

    r = row
    c = col
    # direction up-left
    while r != 0 and c != 0:
        r = r - 1
        c = c - 1
        yield r,c

    r = row
    c = col
    # direction down-left
    while c != 0 and r != n-1:
        r = r + 1
        c = c - 1
        yield r,c
    
    r = row
    c = col
    # direction down-right
    while c != n-1 and r != n-1:
        r = r + 1
        c = c + 1
        yield r,c    

if __name__ == "__main__":
    main()