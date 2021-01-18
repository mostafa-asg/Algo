#User function Template for python3

def longestSubsequence(arr,arr_size):
    lengths = [1] * arr_size
    longest = 1 if arr_size > 0 else 0

    for j in range(1, arr_size):
        for i in range(0, j):
            if arr[j] > arr[i]:
                if lengths[i] + 1 > lengths[j]:
                    lengths[j] = lengths[i] + 1
                    if lengths[j] > longest:
                        longest = lengths[j]

    return longest


    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        print(longestSubsequence(a,n))
# } Driver Code Ends