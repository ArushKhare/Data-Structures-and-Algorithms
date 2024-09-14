class DisjointSet():
    def __init__(self, n):
        self.n = n
        self.nodes = [i for i in range(0, n)]
        self.parent = [i for i in range(0, n)]
        self.rank = [0 for _ in range(0, n)]
    
    def __repr__(self):
        return str(self.nodes)

    def get_parent_list(self):
        return self.parent

    def get_parent(self, i):
        if self.parent[i] == self.parent[self.parent[i]]:
            return i
        while self.parent[i] != self.parent[self.parent[i]]:
            i = self.parent[i]
        return i
    
    def union(self, a, b):
        if self.parent[a] == self.parent[b]:
            return False
        if self.rank[a] >= self.rank[b]:
            self.parent[b] = self.get_parent(a)
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1
        else:
            self.parent[a] = self.get_parent(b)
        return True
    

dj_set = DisjointSet(9)

print(dj_set.get_parent_list())

dj_set.union(0, 1)
dj_set.union(1, 2)
dj_set.union(1, 3)
dj_set.union(2, 3)

print(dj_set.get_parent_list())
