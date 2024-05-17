from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start):
        visited = [False] * len(self.graph)
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, node, visited):
        visited[node] = True
        print(node, end=' ')

        for neighbour in self.graph[node]:
            if not visited[neighbour]:
                self._dfs_recursive(neighbour, visited)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    # self.graph = {
    #     0: [1, 2],
    #     1: [2],
    #     2: [0, 3],
    #     3: [3]
    # }

    print("DFS traversal starting from vertex 2:")
    g.dfs(2)