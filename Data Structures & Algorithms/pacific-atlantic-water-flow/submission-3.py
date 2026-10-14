class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        
        pacific = set()
        atlantic = set()
        directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]

        # 反向搜索，记录能流到对应海洋的格子
        def dfs(r, c, reachable):
            # 当前格子已经搜索过，不重复处理
            if (r, c) in reachable:
                return

            reachable.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # 邻居越界，跳过
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # 反向搜索不能走向更低的位置
                if heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, reachable)
        # main:
        # 左边接触太平洋，右边接触大西洋
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        # 上边接触太平洋，下边接触大西洋
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        result = []
        # 找出能流到两个海洋的格子
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result

# 中文思路清单（反向 DFS：从两个海洋的边界搜索，最后取交集）
#
# 1. 检查输入是否为空。
#    - 如果 heights 为空，或者第一行没有格子，返回 []。
#
# 2. 初始化关键变量。
#    - rows、cols：矩阵的行数和列数。
#    - heights[r][c]：坐标 (r, c) 的高度。
#    - pacific：记录水能够流到太平洋的格子坐标。
#    - atlantic：记录水能够流到大西洋的格子坐标。
#    - directions：上下左右四个方向的坐标变化。
#
# 3. 定义 dfs(r, c, reachable)，从当前位置继续反向搜索。
#    - reachable 是当前海洋对应的集合，可以是 pacific 或 atlantic。
#    - 如果 (r, c) 已经在 reachable 中，直接 return，避免重复搜索。
#    - 否则先执行 reachable.add((r, c))，标记当前位置。
#    - 然后逐个检查上下左右的邻居。
#    - nr = r + dr，nc = c + dc：计算邻居坐标。
#    - 如果邻居越界，continue，检查下一个方向。
#    - 如果邻居高度低于当前高度，也 continue。
#    - 否则调用 dfs(nr, nc, reachable)，继续搜索。
#
# 4. 理解反向搜索的高度条件。
#    - 正常水流：从高处流向低处，或者流向相同高度。
#    - 我们从海洋边界出发，倒着追踪哪些格子的水能够流过来。
#    - 因此，只能搜索高度大于或等于当前高度的邻居。
#    - 代码中遇到 heights[nr][nc] < heights[r][c] 就跳过。
#    - 例如，从高度 2 的边界格子反向走到高度 5：
#      因为真实的水能够从 5 流到 2，再流入海洋。
#    - 反向搜索向高处走，不表示真实的水能够向高处流。
#
# 5. 遍历每一行，从左右边界启动搜索。
#    - dfs(r, 0, pacific)：左边界直接接触太平洋。
#    - dfs(r, cols - 1, atlantic)：右边界直接接触大西洋。
#    - 边界格子本身就能流入对应海洋，所以直接作为起点。
#
# 6. 遍历每一列，从上下边界启动搜索。
#    - dfs(0, c, pacific)：上边界直接接触太平洋。
#    - dfs(rows - 1, c, atlantic)：下边界直接接触大西洋。
#    - 同一个海洋的所有搜索起点共享同一个集合。
#    - 角落可能被重复调用，但已访问检查会避免重复搜索。
#
# 7. 遍历所有格子，收集同时属于两个集合的坐标。
#    - 如果 (r, c) in pacific and (r, c) in atlantic，
#      就执行 result.append([r, c])。
#    - 这表示该格子的水既能流到太平洋，也能流到大西洋。
#    - 去两个海洋的路线可以不同。
#    - 最后返回 result。
#
# 8. 容易混淆的地方。
#    - 太平洋接触上边和左边；大西洋接触下边和右边。
#    - 反向搜索允许邻居高度 >= 当前高度，相等也能通过。
#    - 必须分别记录两个海洋的访问结果，不能共用一个 visited 集合。
#    - 先标记当前格子，再搜索邻居，避免等高格子之间来回递归。
#    - 不需要在递归结束后删除坐标，要一直保留搜索结果。
#    - 不修改 heights，因为两个海洋的搜索都需要原始高度。
#    - 高度 0 也是合法格子，不代表障碍或者水域。
#    - DFS 通过更新集合保存结果，不需要返回 True、False 或面积。
#    - 集合里存元组 (r, c)，最终答案里存列表 [r, c]。
#    - 最终取交集：必须同时属于两个集合，只属于一个不够。
#
# 9. 时间和空间复杂度。
#    - 假设矩阵有 m 行、n 列。
#    - 时间复杂度：O(m * n)。
#      每个格子对每个海洋最多访问一次，每次检查四个方向。
#      虽然从多个边界启动 DFS，但共享集合可以避免重复搜索。
#      最后再扫描一次矩阵，总时间仍然是 O(m * n)。
#    - 空间复杂度：O(m * n)。
#      两个集合和递归调用栈，最坏都需要 O(m * n) 空间。
#
# 快速记忆思路
# 太平洋从上、左出发，大西洋从下、右出发。
# 反着搜索，只走同高或更高的位置。
# 两个集合分别记录，最后找交集。
#
# 口语讲述思路
#
# I'll use DFS to search backward from the ocean borders.
#
# I'll keep two sets: one for cells that can reach the Pacific
# and one for cells that can reach the Atlantic.
#
# The Pacific touches the top and left borders,
# so I start Pacific searches from those cells.
# The Atlantic touches the bottom and right borders,
# so I start Atlantic searches from those cells.
#
# In DFS, I return if the cell is already in the current ocean's set.
# Otherwise, I mark it as visited and check its four neighbors.
#
# I skip neighbors that are out of bounds or lower than the current cell.
# Since I'm searching backward, I only move to equal or higher cells.
# Water can flow from those neighbors back to the current cell
# and then follow the existing path to the ocean.
#
# I mark each cell before exploring its neighbors
# to avoid visiting the same cell repeatedly.
#
# After both searches finish, I scan the grid
# and add every cell that appears in both sets to the result.
# Those are the cells where water can reach both oceans.
#
# The time complexity is O(m * n), where m and n are the grid dimensions.
# Each cell is visited at most once for each ocean.
# The space complexity is also O(m * n)
# for the two sets and the recursion stack.