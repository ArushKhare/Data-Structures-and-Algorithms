# Undirected Graph
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

def mirror(edge: Edge):
    return Edge(edge.end, edge.start, edge.dist)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

e12 = Edge(node1, node2, 6)
e21 = mirror(e12)
e15 = Edge(node1, node5, 2)
e51 = mirror(e15)
e23 = Edge(node2, node3, 7)
e32 = mirror(e23)
e24 = Edge(node2, node4, 1) 
e42 = mirror(e24) 
e37 = Edge(node3, node7, 1) 
e73 = mirror(e37) 
e38 = Edge(node3, node8, 3) 
e83 = mirror(e38) 
e56 = Edge(node5, node6, 3) 
e65 = mirror(e56) 
e67 = Edge(node6, node7, 2) 
e76 = mirror(e67) 
e79 = Edge(node7, node9, 10) 
e97 = mirror(e79) 
e89 = Edge(node8, node9, 2) 
e98 = mirror(e89)

# Create mirror edges too
node1.edges = [e12, e15]
node2.edges = [e21, e23, e24]
node3.edges = [e32, e37, e38]
node4.edges = [e42]
node5.edges = [e51, e56]
node6.edges = [e65, e67]
node7.edges = [e73, e76, e79]
node8.edges = [e83, e89]
node9.edges = [e97, e98]

print(dijkstra(node1, 9))
