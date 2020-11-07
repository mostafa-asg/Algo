def main():
    t = int(input())

    for _ in range(t):
        row, col = map(int, input().split())
        input_matrix = input().split()
        matrix = []
        for r in range(row):
            new_row = []
            for c in range(col):
                new_row.append(input_matrix[r*col+c])
            matrix.append(new_row)
        
        x, y, k = map(int, input().split())
        start_fill(matrix, x, y, k)
        print_matrix(matrix)


def print_matrix(matrix):
    result = []
    for row in range(len(matrix)):
        result.append(" ".join(map(str, matrix[row])))
    print(" ".join(result))


def start_fill(matrix, x, y, k):
    old_color = matrix[x][y]
    fill(matrix, x, y, k, old_color)

def fill(matrix, x, y, k, old_color):
    if x < 0 or y < 0:
        return
    try:        
        if matrix[x][y] == old_color:
            matrix[x][y] = k
            
            fill(matrix, x-1, y, k, old_color)
            fill(matrix, x+1, y, k, old_color)
            fill(matrix, x, y-1, k, old_color)
            fill(matrix, x, y+1, k, old_color)
    except IndexError:
        # Out of boundary, do nothing
        pass

                

if __name__ == "__main__":
    main()