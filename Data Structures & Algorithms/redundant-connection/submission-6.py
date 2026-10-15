class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 题目中节点数和边数相同
        n = len(edges)

        # 节点编号为 1 到 n，下标 0 不使用
        parent = list(range(n + 1)) #parent = [0, 1, 2, 3, 4]
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

            # # 让 root_a 对应较大的集合
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            # 把较小的集合合并到较大的集合
            parent[root_b] = root_a
            size[root_a] += size[root_b]

        #return []

# 找到 a 的组长
# 找到 b 的组长
# 如果组长相同，说明它们已经相通
# 再添加这条边就会形成环，因此返回这条边

# 中文思路清单（并查集：查组长，判断连通，合并小组）
#
# 1. 确定节点数量。
#    - n = len(edges)。
#    - 原来的树有 n 个节点、n - 1 条边，增加一条边后共有 n 条边。
#    - 因此，这道题的节点数量与输入边数相同。
#
# 2. 初始化 parent 和 size。
#    - parent = list(range(n + 1))。
#    - 节点编号为 1 到 n，所以多开一个位置，下标 0 不使用。
#    - 初始 parent[i] = i：每个节点自己当组长，单独组成一组。
#    - parent[i] 表示找组长时，节点 i 应该继续找谁。
#    - size = [1] * (n + 1)：每组最开始只有一个节点。
#    - size[root] 保存以 root 为组长的那组有多少个节点。
#
# 3. 定义 find(node)，找到节点最终所属的组长。
#    - 如果 parent[node] == node，说明自己就是组长，直接返回。
#    - 否则，递归调用 find(parent[node])，继续向上找。
#    - 找到最终组长后，执行 parent[node] = 最终组长。
#    - 最后返回 parent[node]，也就是组长编号。
#    - 这个直接登记最终组长的操作叫路径压缩，让后续查找更快。
#    - find 返回的是节点编号，不是 True 或 False。
#
# 4. 按输入顺序，逐条处理边 [a, b]。
#    - root_a = find(a)：找到节点 a 的组长。
#    - root_b = find(b)：找到节点 b 的组长。
#    - 两个节点组长相同，就表示通过之前处理的边，它们已经相通。
#
# 5. 如果 root_a == root_b，直接返回当前边。
#    - 两个端点之间已经存在路径，再加入这条边就会形成环。
#    - 返回 [a, b]，不是返回 [root_a, root_b]。
#    - 找到答案后，整个函数立即结束。
#
# 6. 如果组长不同，先决定合并后的组长。
#    - 比较 size[root_a] 和 size[root_b]。
#    - 如果 root_a 的组更小，就交换 root_a、root_b 两个变量。
#    - 交换后，root_a 对应较大的组，root_b 对应较小的组。
#    - 大小相同时，保持原来的顺序即可。
#    - 这里只交换根编号变量，不修改原来的 a、b。
#
# 7. 合并两个组，并更新人数。
#    - parent[root_b] = root_a：让小组的组长跟着大组的组长。
#    - 小组的其他成员也就最终归到 root_a 这一组。
#    - size[root_a] += size[root_b]：更新合并后的总人数。
#    - 合并后，继续处理下一条输入边。
#
# 8. 理解为什么直接返回的边符合“最后出现”的要求。
#    - 题目保证原图是一棵树，只增加了一条边，所以只有一个环。
#    - 按输入顺序处理时，环上的最后一条边出现，环才会闭合。
#    - 因此，第一次检测到两端已经连通的边，
#      就是唯一环中在输入里最后出现的边。
#    - 它不一定是整个 edges 列表的最后一条边。
#
# 9. 如果遍历结束仍未发现答案，返回 []。
#    - 这是兜底返回。
#    - 题目保证存在冗余边，因此合法输入会在循环中找到答案。
#
# 10. 容易混淆的地方。
#     - list(range(n + 1)) 用圆括号调用 list，不能写成 list[range(...)]。
#     - “一组”表示目前已经互相连通的节点，不需要真的创建 Python set。
#     - parent[node] 可能是中间联系人，find(node) 才是最终组长。
#     - 必须比较 find 的结果，不能只比较两个节点当前的 parent 值。
#     - size 要用根编号读取：size[root_a]、size[root_b]。
#       普通成员位置的 size 可能保留旧值，不能代表整个组的人数。
#     - 两个组都合并到根节点上，不能随意修改普通成员的 parent 来合并。
#     - parent 记录并查集内部的关系，不代表原图中一定存在对应的边。
#     - 无向边 [a, b] 与 [b, a] 表示同一条连接，代码都能处理。
#     - 按大小合并和路径压缩用于提高效率，不改变节点之间的连通关系。
#
# 11. 时间和空间复杂度。
#     - 这里节点数与边数都是 n。
#     - 时间复杂度：O(n * α(n))。
#       使用路径压缩和按大小合并后，单次操作的均摊时间接近常数。
#       α(n) 增长极慢，所以整体接近线性时间。
#     - 空间复杂度：O(n)。
#       用于 parent、size 数组和 find 的递归调用栈。
#
# 快速记忆思路
# 每个点先自己一组 → 每条边先查两端组长。
# 组长相同：已经相通，再连就成环，返回当前边。
# 组长不同：小组合并到大组，更新人数，继续检查。
#
# 口语讲述思路
#
# I'll use Union Find to track which nodes are connected.
# Initially, every node is in its own group.
#
# The find function returns a node's root, which represents its group.
# I use path compression so that nodes point directly to their final root
# after a lookup.
#
# Then I process the edges in input order.
# For each edge, I find the roots of its two endpoints.
#
# If the roots are the same, the endpoints are already connected.
# Adding this edge would create a cycle, so I return the original edge.
#
# If the roots are different, I merge the two groups.
# I attach the smaller group's root to the larger group's root
# and update the combined size.
#
# The graph has exactly one cycle.
# That cycle only closes when its last edge in input order is processed.
# So the first edge I detect as redundant is the required answer.
#
# With path compression and union by size,
# the total time complexity is O(n * alpha(n)), which is close to linear.
# The space complexity is O(n) for the arrays and the recursion stack.
