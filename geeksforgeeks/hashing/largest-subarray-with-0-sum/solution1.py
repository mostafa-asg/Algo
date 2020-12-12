#Your task is to complete this function
#Your should return the required output
def maxLen(n, arr):
    sums = dict()
    sum = 0
    max_length = 0

    for i in range(0, len(arr)):
        sum += arr[i]

        if sum == 0:
            if max_length < i:
                max_length = i + 1
        elif sum in sums:
            if max_length < i-sums[sum]:
                max_length = i-sums[sum]
        else:
            sums[sum] = i

    return max_length




#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends