class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1)) #用圆括号！
        size = [1] * (n+1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]



        for a,b in edges:
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return [a,b]
                
            if size[root_a] < size[root_b]: #不是size[a] < size[b]
                root_a , root_b = root_b, root_a

            parent[root_b] = root_a 
            size[root_a] += size[root_b]
            
        #return []

# 第一处，创建列表时应该使用圆括号：
# parent = list[range(n + 1)]  # 这里写错了
# 改成：
# parent = list(range(n + 1))
# list(...) 是调用 list，把 range 转成列表。

