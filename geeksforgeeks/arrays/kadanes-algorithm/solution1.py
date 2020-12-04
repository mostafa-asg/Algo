#User function Template for python3

##Complete this function
def maxSubArraySum(arr,size):
    if len(arr) == 0:
        return 0
    
    max_ = arr[0]
    sub_array_max = arr[0]

    if len(arr) > 1:
        for i in range(1, len(arr)):
            sub_array_max = max(arr[i], sub_array_max+arr[i])
            if sub_array_max > max_:
                max_ = sub_array_max

    return max_



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            print(maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends