class UnionAndFind:
    def __init__(self, n):
        self.parent = list(range(n))
        # Initially ranks are zero for all vertices
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            # Path compression
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.parent[u]
        root_v = self.parent[v]

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.parent[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] = self.rank[root_u] + 1
            # No cycle detected
            return False
        else:
            # Cycle detected
            return True


# Example usage:
if __name__ == "__main__":
    n = 5  # Number of elements
    ds = UnionAndFind(n)

    ds.union(0, 2)
    ds.union(4, 2)
    ds.union(3, 1)

    print("Find(4):", ds.find(4))
    print("Find(3):", ds.find(3))

    ds.union(3, 2)

    print("Find(3) after union with 2:", ds.find(3))
