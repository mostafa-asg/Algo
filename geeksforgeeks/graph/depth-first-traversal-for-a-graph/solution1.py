#User function Template for python3

'''
g : adjacency list of graph
N : number of vertices

return a list containing the DFS traversal of the given graph
'''

def dfs(g,N):
    seen_before = [False for _ in range(N)]
    traverse_list = []
    do_dfs(0, g, seen_before, traverse_list)
    return traverse_list

def do_dfs(v, g, seen_before, traverse_list):
    if seen_before[v] == False:
        traverse_list.append(v)
        seen_before[v] = True

        for other_v in g[v]:
            do_dfs(other_v, g, seen_before, traverse_list)



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

#Contributed by : Nagendra Jha

#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N,E = map(int,input().strip().split())
        g = Graph(N)
        edges = list(map(int,input().strip().split()))

        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) # add an undirected edge from u to v
            g.addEdge(v,u)

        res = dfs(g.graph,N)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()

# } Driver Code Ends