def main():
    test_case = int(input())
    for _ in range(test_case):
        input() # strings size
        s1 = input()
        s2 = input()
        size = find_longest_common_substring_size(s1, s2)
        print(size)

def find_longest_common_substring_size(s1: str, s2: str) -> int:
    arr = []
    max_value = 0
    rows = len(s1) + 1
    cols = len(s2) + 1
    
    for i in range(rows):
        arr.append([0] * cols)

    for row in range(1,rows):
        for col in range(1,cols):
            if s1[row-1] == s2[col-1]:
                arr[row][col] = 1 + arr[row-1][col-1]
                if arr[row][col] > max_value:
                    max_value = arr[row][col]
            else:
                arr[row][col] = 0

    return max_value

if __name__ == "__main__":
    main()