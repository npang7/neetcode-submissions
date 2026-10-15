class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return False


        graph = [[] for _ in range(n)] #给每个节点创建一个邻居列表
        for a, b in edges:  #记录邻居
            graph[a].append(b)
            graph[b].append(a)

        visited = set()


        # 当前搜索没有发现环，返回 True；发现环，返回 False
        def dfs(node, parent):
            if node in visited: #发现环
                return False

            visited.add(node)

            for neighbor in graph[node]:
                # 不沿着刚才的边走回去
                if neighbor == parent:
                    continue

                # 邻居方向发现环，向上一层返回 False
                if not dfs(neighbor, node):
                    return False

            return True


        # 从节点 0 开始，它没有父节点，用 -1 表示
        if not dfs(0, -1):
            return False

        # 没有环之后，还要确认所有节点都连通
        return len(visited) == n