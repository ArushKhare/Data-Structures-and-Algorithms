class DisjointSet():
    def __init__(self, n):
        self.nodes = [i for i in range(0, n)]
        self.parent = [i for i in range(0, n)]
        self.rank = [0 for _ in range(0, n)]
    
    def __repr__(self):
        return str(self.nodes)

    def get_parent_list(self):
        return self.parent

    def get_parent(self, i):
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

print("Initial Parent List:", dj_set.get_parent_list())

print("Did 0 and 1 unite?:", dj_set.union(0, 1)) # 0 -> 1 (UNION WORKS)
print("Did 1 and 2 unite?:", dj_set.union(1, 2)) # 1 -> 2 (UNION WORKS)
print("Did 1 and 3 unite?:", dj_set.union(1, 3)) # 1 -> 3 (UNION WORKS)
print("Did 2 and 3 unite?:", dj_set.union(2, 3)) # 2 -/> 3 (UNION FAILS)

print("Final Parent List:", dj_set.get_parent_list())
