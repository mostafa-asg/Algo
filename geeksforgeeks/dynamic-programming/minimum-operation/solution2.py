#User function Template for python3

class Solution:
    def minOperation(self, n):
        base_case = [0, 1, 2, 3]

        if n <= 3:
            return base_case[n]
        
        ops_count = 0    
        quotient = n
        
        while quotient > 3:    
            quotient, reminder = divmod(quotient , 2)
            if quotient > 1:
                ops_count = ops_count + 1
            ops_count = ops_count + reminder

        return ops_count + base_case[quotient]


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