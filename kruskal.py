class Edge():
    def __init__(self, vertexA, vertexB, weight):
        self.vertexA = vertexA
        self.vertexB = vertexB
        self.weight = weight

    def __repr__(self):
        return str((self.vertexA, self.vertexB, self.weight))


class DisjointSet():
    def __init__(self, n):
        self.parent = [-1 for i in range(0, n)]
        self.rank = [0 for _ in range(0, n)]

    def get_parent_list(self):
        return self.parent

    def get_parent(self, i):
        while self.parent[i] != -1:
            i = self.parent[i]
        return i
    
    def union(self, a, b):
        parentA = self.get_parent(a)
        parentB = self.get_parent(b)

        if (parentA == parentB):
            return False

        if self.rank[parentA] > self.rank[parentB]:
            self.parent[b] = parentA
        elif self.rank[parentA] == self.rank[parentB]:
            self.rank[parentA] += 1
            self.parent[b] = parentA
        else:
            self.parent[a] = parentB
        
        return True


class Graph():
    def __init__(self, n):
        self.djset = DisjointSet(n)
        self.edges = []

    def add_edge(self, vertexA, vertexB, weight):
        self.edges.append(Edge(vertexA, vertexB, weight))
    
    def kruskal_mst(self):
        mst = []
        self.edges.sort(key=lambda x: x.weight)
        for edge in self.edges:
            joined = self.djset.union(edge.vertexA, edge.vertexB)
            if joined:
                mst.append(edge)
        
        return mst
    

if __name__ == '__main__':
    graph = Graph(8)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 6, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(0, 7, 9)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 6)
    graph.add_edge(1, 5, 4)
    graph.add_edge(2, 6, 10)
    graph.add_edge(2, 7, 3)
    graph.add_edge(3, 5, 8)
    graph.add_edge(4, 5, 7)
    graph.add_edge(4, 7, 11)
    graph.add_edge(5, 6, 4)
    print(graph.kruskal_mst())
