# Use subtraction to check the answer
# If the result is 0, this is the answer
# If the result is negative, no need to go to the end of array

def find_subarray_with_given_sum(arr, sum):
    for i in range(len(arr)):
        sub = sum
        for j in range(i,len(arr)):
            sub = sub - arr[j]
            if sub == 0:
                return i, j 
            
            if sub < 0:
                break

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