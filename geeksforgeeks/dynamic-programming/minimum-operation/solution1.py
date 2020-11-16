#User function Template for python3

class Solution:
    def minOperation(self, n):
        if n <= 3:
            return n
        
        ops_count = 0        
        quotient, reminder = divmod(n , 2)
        if quotient > 1:
            ops_count = ops_count + 1
        ops_count = ops_count + reminder

        return ops_count + self.minOperation(quotient)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends