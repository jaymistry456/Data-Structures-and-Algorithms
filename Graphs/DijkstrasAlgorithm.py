import sys


class Graph:
    def __init__(self, N):
        self.N = N
        self.graph = [[0 for _ in range(N)] for _ in range(N)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def min_distance(self, distance, sp_set):
        min_value = sys.maxsize
        min_index = -1

        for i in range(self.N):
            if distance[i] < min_value and not sp_set[i]:
                min_value = distance[i]
                min_index = i
        return min_index

    def dijkstra(self, src):
        distance = [sys.maxsize] * self.N
        parent = [-1] * self.N
        sp_set = [False] * self.N

        distance[src] = 0

        for _ in range(self.N - 1):
            parent_index = self.min_distance(distance, sp_set)
            sp_set[parent_index] = True

            for adj_index in range(self.N):
                if self.graph[parent_index][adj_index] > 0 and not sp_set[adj_index] and self.graph[parent_index][adj_index] + distance[parent_index] < distance[adj_index]:
                    distance[adj_index] = distance[parent_index] + self.graph[parent_index][adj_index]
                    parent[adj_index] = parent_index

        self.print_sp(distance)

    def print_sp(self, distance):
        print("Vertex \t Distance from Source")
        for node in range(self.N):
            print(node, "\t\t", distance[node])

# Example usage:
if __name__ == "__main__":
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 5, 4)
    g.add_edge(2, 8, 2)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

    g.dijkstra(0)
