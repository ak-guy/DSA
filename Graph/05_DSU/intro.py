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

    def unionBySize(self, x: int, y: int):
        rootX = self.findParent(x)
        rootY = self.findParent(y)

        if rootX == rootY:
            return

        if self.size[rootX] > self.size[rootY]:
            self.size[rootX] += self.size[rootY]
            self.parent[rootY] = rootX
        else:
            self.size[rootY] += self.size[rootX]
            self.parent[rootX] = rootY


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
