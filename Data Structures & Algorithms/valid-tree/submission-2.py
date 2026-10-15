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

# 中文思路清单（DFS：检查无环 + 检查连通）
#
# 1. 处理没有节点的情况。
#    - 如果 n == 0，这份实现返回 False。
#    - 合法的树需要满足两个条件：所有节点连通，并且没有环。
#
# 2. 建立无向图的邻接表。
#    - graph = [[] for _ in range(n)]。
#    - graph[i] 保存节点 i 的所有邻居。
#    - 对每条边 [a, b]，把 b 加入 graph[a]，把 a 加入 graph[b]。
#    - 因为边是无向的，所以两个方向都要记录。
#
# 3. 创建 visited 集合。
#    - visited 保存已经访问过的节点编号。
#    - 用来检测重复访问，也用来统计最终访问到多少个节点。
#
# 4. 从节点 0 开始调用 dfs(0, -1)。
#    - dfs(node, parent)：检查从当前节点继续搜索时是否发现环。
#    - node：当前节点。
#    - parent：这次是从哪个节点走过来的。
#    - 起点没有父节点，用 -1 表示，不会与合法节点编号冲突。
#    - 节点 0 只是任选的搜索起点，不是题目指定的树根。
#
# 5. 每次进入 DFS，先检查当前节点是否已经访问过。
#    - 如果 node in visited，返回 False，表示发现环。
#    - 正常走回父节点的情况，会在递归调用前被跳过。
#    - 因此，实际再次进入一个已访问节点时，是通过其他连接绕回来的。
#    - 如果没有访问过，就执行 visited.add(node)。
#    - 必须先标记，再搜索邻居，才能识别后续的重复访问。
#
# 6. 遍历当前节点的所有邻居。
#    - 如果 neighbor == parent，使用 continue 跳过。
#    - 沿同一条无向边走回刚才的节点，不算形成环。
#    - 对其他邻居调用 dfs(neighbor, node)。
#    - 下一层的当前节点是 neighbor，父节点是当前的 node。
#
# 7. 根据邻居搜索的结果，决定是否继续。
#    - 如果 dfs(neighbor, node) 返回 False，当前层也立即返回 False。
#    - 发现环的结果会一层层传回主函数。
#    - 如果返回 True，就继续检查其他邻居。
#    - 所有邻居检查完成后，当前层才返回 True。
#    - return True 必须放在邻居 for 循环外面。
#
# 8. DFS 结束后，在主函数中判断最终结果。
#    - 如果 dfs(0, -1) 返回 False，直接返回 False。
#    - 否则，只能说明从节点 0 到达的这一部分没有环。
#    - 还需要检查 len(visited) == n，确认访问了全部节点。
#    - 如果相等，说明所有节点连通，返回 True。
#    - 如果不相等，说明存在无法从 0 到达的节点，返回 False。
#
# 9. 容易混淆的地方。
#    - 这里是普通的树，不要求是二叉树，一个节点可以有多个邻居。
#    - parent 是搜索过程中的上一个节点，不是节点原本自带的属性。
#    - 不能把所有已访问的邻居都直接跳过，否则可能漏掉环。
#      只跳过 parent，遇到其他已访问节点时要判定有环。
#    - DFS 返回 True，不代表整张图已经连通。
#      必须再检查 visited 的大小是否等于 n。
#    - return 只结束当前这次函数调用。
#      某个邻居返回 True 后，上一层还需要继续检查其他邻居。
#    - 不需要在递归结束后从 visited 删除节点。
#      我们要一直保留访问记录，用于检测环和判断连通性。
#    - 一个节点、没有边，是合法的树。
#    - 多个节点、没有边，不连通，因此不是树。
#
# 10. 时间和空间复杂度。
#     - V = n：节点数量。
#     - E = len(edges)：边的数量。
#     - 时间复杂度：O(V + E)。
#       建立邻接表后，每个节点最多首次访问一次，
#       每条无向边最多从两个方向各检查一次。
#     - 空间复杂度：O(V + E)。
#       邻接表需要 O(V + E)，visited 和递归栈最多需要 O(V)。
#
# 快速记忆思路
# 无向边双向存 → DFS 记录访问 → 跳过父节点 → 再遇已访问节点就是环。
# 搜索无环还不够，最后检查是否访问了全部 n 个节点。
# 一棵树 = 连通 + 无环。
#
# 口语讲述思路
#
# A valid tree must be connected and have no cycles.
# I'll check both conditions using DFS.
#
# First, I build an adjacency list.
# Since the graph is undirected, I add each edge in both directions.
#
# Then I start DFS from node zero and keep a visited set.
# I also pass the parent node into each DFS call.
# For the starting node, I use minus one as the parent.
#
# In DFS, I mark the current node as visited and explore its neighbors.
# I skip the parent because going back along the same edge is not a cycle.
#
# If I reach an already visited node through another edge,
# I have found a cycle, so I return false.
# That false result is passed back through the recursive calls.
#
# If all neighbors are checked without finding a cycle,
# the current DFS call returns true.
#
# After DFS finishes, I check whether the visited set contains all n nodes.
# If any nodes are missing, the graph is disconnected, so I return false.
# If all nodes were visited and no cycle was found, I return true.
#
# The time complexity is O(V + E),
# where V is the number of nodes and E is the number of edges.
# The space complexity is also O(V + E)
# for the adjacency list, the visited set, and the recursion stack.
