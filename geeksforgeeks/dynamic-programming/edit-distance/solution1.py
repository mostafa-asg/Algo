class Solution:

    def editDistance(self, s, t):        
        distance = []

        for i in range(len(t) + 1):
            arr = [0] * (len(s) + 1)
            distance.append(arr)

        s1 = list(s)
        s1.insert(0, '')

        t1 = list(t)
        t1.insert(0, '')

        for i in range(len(s) + 1):
            distance[0][i] = i

        for i in range(len(t) + 1):
            distance[i][0] = i

        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if s1[j] == t1[i]:
                    distance[i][j] = distance[i - 1][j - 1]
                else:
                    distance[i][j] = min(distance[i - 1][j - 1],
                            distance[i][j - 1], distance[i - 1][j]) + 1

        return distance[len(t)][len(s)]        


#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends