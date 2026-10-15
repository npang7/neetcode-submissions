class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 题目中节点数和边数相同
        n = len(edges)

        # 节点编号为 1 到 n，下标 0 不使用
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        # 找到 node 所属集合的根节点
        def find(node):
            if parent[node] != node:
                # 路径压缩：直接指向最终的根节点
                parent[node] = find(parent[node])

            return parent[node]

        for a, b in edges:
            root_a = find(a)
            root_b = find(b)

            # 已经连通，再加这条边就会形成环
            if root_a == root_b:
                return [a, b]

            # 让 root_a 对应较大的集合
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            # 把较小的集合合并到较大的集合
            parent[root_b] = root_a
            size[root_a] += size[root_b]

        return []