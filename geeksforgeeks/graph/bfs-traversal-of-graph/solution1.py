#User function Template for python3

'''
*  g[]: adj list of the graph
*  N : number of vertices
'''
def bfs(g,N):
    explore = [0]
    seen = dict()
    result = [0]
    
    while len(explore) > 0:
        v = explore.pop(0)
        if seen.get(v, False) == False:
            seen[v] = True
            result.append(v)
            for item in g[v]:
                explore.append(item)
                
    return result



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict
import queue
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
            g.addEdge(u,v) # add a directed edge from u to v

        res = bfs(g.graph,N) # print bfs of graph
        for i in range (len (res)):
            print (res[i], end = " ")
        print()

# } Driver Code Ends