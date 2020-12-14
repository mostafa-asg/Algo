# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices
def isCyclic(n, graph):
    # Code here
    detector = CycleDetector(graph)
    return detector.isCyclic()


class CycleDetector():

    def __init__(self, graph: dict):
        self.graph = graph
        self.seen = set()

    def isCyclic(self):
        vertices = set(graph.keys())

        for vertex in vertices:
            if not vertex in self.seen:
                seen_vertices = []
                
                result = self._expand(vertex, seen_vertices)
                if result == True:
                    return True

        return False

    def _expand(self, vertex, seen_vertices):
        seen_vertices.append(vertex)
        self.seen.add(vertex)

        for v in self.graph[vertex]:
            if v in seen_vertices:
                return True
            else:
                result = self._expand(v, seen_vertices)
                if result == True:
                    return True
            seen_vertices.pop()

        return False

#{ 
#  Driver Code Starts

from collections import defaultdict

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)
# } Driver Code Ends