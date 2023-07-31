# Directed Graph
class Node:
    def __init__(self, id, edges=[]):
        self.edges = edges
        self.id = id
        self.dist = 0
    
    def __str__(self):
        return str(self.id)

class Edge:
    def __init__(self, start, end, dist):
        self.start = start
        self.end = end
        self.dist = dist
    
    def __str__(self):
        return str([self.start, self.end, self.dist])

def dijkstra(root: Node, size: int):
    stack = [root]
    vis = set()
    vis.add(root)
    distances = [float('inf')] * size
    distances[root.id-1] = 0

    while stack:
        curr = stack.pop(0)
        for edge in curr.edges:
            distances[edge.end.id-1] = min(distances[edge.end.id-1], distances[curr.id-1] + edge.dist)
            if edge.end not in vis:
                stack.append(edge.end)
                vis.add(edge.end)
    
    return distances

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

node1.edges = [Edge(node1, node2, 6), Edge(node1, node5, 2)]
node2.edges = [Edge(node2, node3, 7), Edge(node2, node4, 1)]
node3.edges = [Edge(node3, node7, 1), Edge(node3, node8, 3)]
node5.edges = [Edge(node5, node6, 3)]
node6.edges = [Edge(node6, node7, 2)]
node7.edges = [Edge(node7, node9, 10)]
node8.edges = [Edge(node8, node9, 2)]

print(dijkstra(node1, 9))
