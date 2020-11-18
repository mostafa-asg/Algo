#User function Template for python3
class Solution:

	def countTriplet(self, arr, n):
        size = len(arr)
        counter = 0

        bag = set()
        for item in arr:
            bag.add(item)

        for i in range(size):
            for j in range(i+1, size):
                if arr[i] + arr[j] in bag:
                    counter = counter + 1

        return counter		



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]

		ob = Solution()
		ans = ob.countTriplet(arr, n)
		print(ans)

# } Driver Code Ends