#User function Template for python3

class Cell():
    def __init__(self, grid, row, col, box_num, possible_values: list):
        self.row = row
        self.col = col
        self.box_num = box_num
        self.possible_values = possible_values
        self.index = 0
        self.grid = grid


    def empty(self):
        self.grid[self.row][self.col] = 0
    

    def put_if_possible(self):
        self.empty()

        while self.index < len(self.possible_values):
            if self.is_safe_to_put(self.possible_values[self.index]):
                self.grid[self.row][self.col] = self.possible_values[self.index]
                self.index += 1            
                return True
            else:
                self.index += 1

        return False

    def reset(self):
        self.empty()
        self.index = 0


    def is_safe_to_put(self, value: int) -> bool:
        box_num = get_box_num(self.row, self.col)

        # row wise
        for i in range(9):
            if grid[self.row][i] == value:
                return False

        # col wise
        for i in range(9):
            if grid[i][self.col] == value:
                return False

        # box wise
        for r, c in get_box_cells(box_num):
            if grid[r][c] == value:
                return False

        return True



def get_box_num(row: int, col: int) -> int:
    r = row // 3
    c = col // 3
    return r*3 + c


box_cells = {
    0: [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)],
    1: [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)],
    2: [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)],
    
    3: [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)],
    4: [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)],
    5: [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)],

    6: [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)],
    7: [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)],
    8: [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)]
}


def get_box_cells(bux_num: int):
    return box_cells[bux_num]


def find_possible_values(grid, row, col) -> list:
    box_num = get_box_num(row, col)
    result = [i for i in range(1,10)]

    # row wise
    for i in range(9):
        if grid[row][i] in result:
            result.remove(grid[row][i])

    # col wise
    for i in range(9):
        if grid[i][col] in result:
            result.remove(grid[i][col])

    # box wise
    for r, c in get_box_cells(box_num):
        if grid[r][c] in result:
            result.remove(grid[r][c])

    return result
            

def solve_sudoku(grid):
    cells = []
    
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                box_num = get_box_num(row, col)
                possible_values = find_possible_values(grid, row, col)
                if len(possible_values) == 0:
                    return False                    
                cells.append(Cell(grid, row, col, box_num, possible_values))

    return _solve_sudoku(cells, 0)


def _solve_sudoku(cell_list, index: int):
    
    while True:
        done = cell_list[index].put_if_possible()
        
        if done == False and index == 0:
            return False

        if done == True and index == len(cell_list)-1:
            return True

        if done == True and index < len(cell_list):
            result = _solve_sudoku(cell_list, index+1)
            if result:
                return True
            else:
                continue
        else:
            cell_list[index].reset()
            return False
    


def print_grid(arr):
    for row in range(9):
        for col in range(9):
            print(arr[row][col], end=" ")    
    print("")



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
            
        if(solve_sudoku(grid)==True):
            print_grid(grid)
        else:
            print("No solution exists")
        t = t-1

# } Driver Code Ends