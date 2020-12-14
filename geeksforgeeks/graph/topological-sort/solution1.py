# Your task is to complete this function
# Function should return Topologically Sorted List
# Graph(adj) is a defaultict of type List
# n is no of edges
def topoSort(n, graph: dict):
    vertecies = {i for i in range(n)}
    seen_vertecies = set()
    result = []

    while len(vertecies) > 0:
        expand(graph, vertecies.pop(), vertecies, seen_vertecies, result)

    return result
        


def expand(graph, vertex, explore: set, seen_vertecies: set, result: list):
    if not vertex in seen_vertecies:

        seen_vertecies.add(vertex)

        try:
            explore.remove(vertex)
        except KeyError:
            pass

        for child in graph[vertex]:
            expand(graph, child, explore, seen_vertecies, result)

        result.insert(0, vertex)





#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
def creategraph(e, n, arr, graph):
    i = 0
    while i<2*e:
        graph[arr[i]].append(arr[i+1])
        i+=2
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

from collections import defaultdict
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)
        
        if check(graph, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends