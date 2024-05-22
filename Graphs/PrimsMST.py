import sys


class Prim:
    def __init__(self, N):
        # N = number of vertices
        self.N = N
        # Initializing an adjacency matrix
        self.graph = [[0 for _ in range(N)] for _ in range(N)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    # Returns the index of the vertex which has the minimum value in the distance array which is not in mst_set
    def min_key(self, distance, mst_set):
        min_value = sys.maxsize
        min_index = -1

        for i in range(self.N):
            if distance[i] < min_value and not mst_set[i]:
                min_index = i
                min_value = distance[min_index]

        return min_index

    def prim_mst(self):
        # Initializing 3 arrays
        # Distance keeps track of the minimum distance of a vertex from its adjacent vertices
        # Parent is the adjacent vertex from where the minimum distance edge was set
        # ms_set includes all the vertices already included in the mst
        distance = [sys.maxsize] * self.N
        parent = [-1] * self.N
        mst_set = [False] * self.N

        # Initializing at vertex 0
        distance[0] = 0

        # Looping the outer loop for N-1 times to find the minimum edge weights
        # For N vertices, there will be N-1 edges between them
        for _ in range(self.N - 1):
            # Three steps are performed N-1 times:
            # 1. Finding the vertex with the minimum distance value in the distance array which is not in mst_set
            # 2. Setting its index to True in mst_set to include it in mst_set
            # 3. For each vertex in the graph, finding the adjacent vertices of this vertex and updating their distances
            #    if the weight between the vertex selected and the adjacent vertex is lower than the corresponding
            #    value stored in the distance array for that particular adjacent vertex.
            parent_index = self.min_key(distance, mst_set)
            mst_set[parent_index] = True

            for adj_index in range(self.N):
                if self.graph[parent_index][adj_index] > 0 and not mst_set[adj_index] and distance[adj_index] > \
                        self.graph[parent_index][adj_index]:
                    distance[adj_index] = self.graph[parent_index][adj_index]
                    parent[adj_index] = parent_index

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.N):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])


# Example usage:
if __name__ == "__main__":
    g = Prim(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    g.prim_mst()
