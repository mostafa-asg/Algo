import functools

def find_subarray_with_given_sum(arr, sum):
    """
    Brute force approach
    """
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            
            # Not efficient, it makes a copy of the original list
            sub_arr = arr[i:j+1]

            computed_sum = functools.reduce(lambda x,y: x+y, sub_arr)
            if (computed_sum == sum):
                return i,j

    return -1,-1

def main():
    test_case_num = int(input())
    for i in range(test_case_num):
        line = input()
        array_size = line.split(" ")[0]
        sum = int(line.split(" ")[1])

        line = input()
        arr = [
            int(item) 
            for item in line.split(" ")                        
            if item # Igonre empty strings
        ]        
        left, right = find_subarray_with_given_sum(arr, sum)
        if left == -1:
            print(-1)
        else:
            # Indexing start from 1
            
            # Python 3.6+
            # print(f"{left+1} {right+1}")

            print("{} {}".format(left+1, right+1))


if __name__ == "__main__":
    main()