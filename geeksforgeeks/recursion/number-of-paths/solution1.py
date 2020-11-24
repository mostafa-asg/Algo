#User function Template for python3

class Solution:
    def numberOfPaths (self, m, n):
        return self.move(1, 1, m, n, 0)

    def move(self, row, col, m, n, counter):
        if row == m and col == n:
            return counter + 1
        else:
            if row < m:
                counter = self.move(row+1, col, m, n, counter)

            if col < n:    
                counter = self.move(row, col+1, m, n, counter)

        return counter



#{ 
#  Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        m, n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)




# } Driver Code Ends