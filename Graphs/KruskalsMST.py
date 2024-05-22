class UnionAndFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] = self.rank[root_u] + 1
            return False
        else:
            return True


class Kruskal:
    def __init__(self, N):
        self.N = N
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def kruskal_mst(self):
        # Sort edges based on weight
        self.edges.sort()

        unionAndFind = UnionAndFind(self.N)

        mst = []
        mst_weight = 0

        for edge in self.edges:
            weight, u, v = edge
            if unionAndFind.union(u, v):
                mst.append((u, v, weight))
                mst_weight = mst_weight + weight

        self.print_mst(mst, mst_weight)

    def print_mst(self, mst, total_weight):
        print("Edges in the MST:")
        for u, v, weight in mst:
            print(f"{u} -- {v} == {weight}")
        print(f"Total weight of MST: {total_weight}")


# Example usage:
if __name__ == "__main__":
    g = Kruskal(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.kruskal_mst()
