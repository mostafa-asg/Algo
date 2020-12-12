#User function Template for python3
def isCyclic(graph,n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    detector = CycleDetector(graph)
    return detector.isCyclic()

class CycleDetector():

    def __init__(self, graph: dict):
        self.graph = graph
        self.seen_vertices = set()

    def isCyclic(self):
        for vertex in self.graph:        
            if not vertex in self.seen_vertices:
                result = self._expand(vertex, expanded_from=vertex)
                if result == 1:
                    return 1

        return 0

    def _expand(self, vertex, expanded_from=None):
        self.seen_vertices.add(vertex)

        for v in self.graph[vertex]:
            if v in self.seen_vertices and v != expanded_from:
                return 1
            elif not v in self.seen_vertices:
                result = self._expand(v, expanded_from=vertex)
                if result == 1:
                    return 1

        return 0

    



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict

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
        print(isCyclic(g.graph,N))
# } Driver Code Ends