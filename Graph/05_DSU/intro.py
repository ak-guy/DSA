class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1 for _ in range(n+1)]

    def findParent(self, node):
        # if parent of node is node itself
        if node == self.parent[node]:
            return self.parent[node]
        
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        ulp_u = self.findParent(u)
        ulp_v = self.findParent(v)
        
        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


if __name__ == "__main__":
    ds = DisjointSet(7)
    ds.unionBySize(1, 2)
    ds.unionBySize(2, 3)
    ds.unionBySize(4, 5)
    ds.unionBySize(6, 7)
    ds.unionBySize(5, 6)
    print(ds.parent)
    print(ds.size)
    # if 3 and 7 same or not
    if ds.findParent(3) == ds.findParent(7):
        print("Same")
    else:
        print("Not Same")

    ds.unionBySize(3, 7)
    if ds.findParent(3) == ds.findParent(7):
        print("Same")
    else:
        print("Not Same")
