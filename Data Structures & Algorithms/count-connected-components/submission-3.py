class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def graph(edges):
            graphs = {}
            for edge in edges:
                a, b = edge
                if a not in graphs:
                    graphs[a] = []
                if b not in graphs:
                    graphs[b] = []
                graphs[a].append(b)
                graphs[b].append(a)
            return graphs
        count = 0
        visited = set()
        graphs = graph(edges)
        def dfs(graphs, current, visited):
            if current in visited:
                return False
            visited.add(current)
            for nei in graphs.get(current, []):
                dfs(graphs, nei, visited)
            return True
        for node in range(n):
            if dfs(graphs, node, visited) == True:
                count+=1
        return count
