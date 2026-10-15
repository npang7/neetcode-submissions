class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        components = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)



        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
                
        return components