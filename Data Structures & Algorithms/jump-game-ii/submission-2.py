#如果这道题“不保证”一定有解
class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        step = 0
        end = 0

        for i in range(len(nums) - 1):
            # 当前位置不可达
            if i > farthest:
                return -1
            
            curr = i + nums[i]
            farthest = max(curr, farthest)
            if i == end:
                end = farthest
                step += 1

        # 循环没有检查终点，因此还需要确认终点是否可达
        if farthest < len(nums) - 1:
            return -1

        return step


# Jump Game II（跳跃游戏 II）
#
# 一、题目理解
#
# 1. nums[i] 表示站在下标 i 时，最多能向右跳多少步。
#    - 可以少跳，不必跳满。
#    - 从下标 0 出发，求到达最后一个下标的最少跳跃次数。
#    - 题目保证一定有解。
#    - 只有一个元素时，起点就是终点，返回 0。
#
# 2. 与 Jump Game 的区别：
#    - Jump Game：能不能到达终点？
#    - Jump Game II：最少跳几次？
#
#
# 二、核心思路：按跳跃次数，逐层扩大可达范围
#
# 1. 不直接选择具体落点，而是维护当前跳数能覆盖的范围。
#
# 2. 检查当前范围内的所有候选位置：
#    - 计算从这些位置再跳一次，最远能到哪里。
#    - 每发现一个更远的位置，只更新最远距离，不立即增加跳数。
#
# 3. 当前这一批位置检查完后：
#    - 跳跃次数加 1。
#    - 把下一跳能覆盖的最远位置设为新的边界。
#
# 4. 为什么是最少跳数？
#    - 先确定 1 跳能覆盖哪里，再确定 2 跳能覆盖哪里……
#    - 按跳跃次数逐层扩展。
#    - 第一次覆盖终点时，对应的就是最少跳数。
#    - 思路类似 BFS 分层，但不需要队列。
#
#
# 三、关键变量
#
# step：
# - 已经确定需要的跳跃次数。
#
# end：
# - 用 step 次跳跃，最远能覆盖的下标。
# - 也是当前这一批候选位置的右边界。
#
# farthest：
# - 根据已检查位置的跳跃能力，目前发现的最远可达下标。
# - 检查当前这一批位置时，用它累计下一跳能覆盖的最远位置。
#
# curr：
# - 从当前位置 i 出发，最远能跳到的下标。
# - curr = i + nums[i]。
#
#
# 四、按照代码执行顺序整理
#
# 1. 初始化。
#    - step = 0：还没跳。
#    - end = 0：跳 0 次，只能站在下标 0。
#    - farthest = 0：初始可达位置是下标 0。
#    - farthest 初始化为 nums[0] 也可以，第一次循环后结果相同。
#
# 2. 遍历下标 0 到倒数第二个下标。
#    - for i in range(len(nums) - 1)。
#    - 每个位置只检查一次，一个 for 循环就够了。
#
# 3. 先更新最远可达位置。
#    - curr = i + nums[i]。
#    - farthest = max(curr, farthest)。
#    - 不能丢掉之前发现的更远位置。
#
# 4. 再判断当前这一批位置是否检查完。
#    - i == end：已经检查到当前范围的右边界。
#    - step += 1：确定需要再跳一次。
#    - end = farthest：更新这一跳能覆盖的边界。
#
# 5. 循环结束，返回 step。
#    - 这里依赖题目保证一定有解。


class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        end = 0
        farthest = 0

        # 只检查到倒数第二个下标
        for i in range(len(nums) - 1):
            curr = i + nums[i]
            farthest = max(curr, farthest)

            # 当前这一批候选位置已经全部检查完
            if i == end:
                step += 1
                end = farthest

        return step


# 五、例子演示
#
# nums = [2, 1, 2, 1, 0]
# 下标：  0  1  2  3  4
#
# 初始：
# step = 0，end = 0，farthest = 0。
#
# i = 0：
# - farthest = max(0, 0 + 2) = 2。
# - i == end，起点这一批检查完。
# - step = 1，end = 2。
# - 含义：1 跳最远可以到下标 2。
#
# i = 1：
# - farthest = max(2, 1 + 1) = 2。
# - i != end，只更新距离，不增加跳数。
#
# i = 2：
# - farthest = max(2, 2 + 2) = 4。
# - i == end，第一跳的候选位置检查完。
# - step = 2，end = 4。
# - 含义：2 跳已经可以到达终点。
#
# i = 3：
# - farthest = max(4, 3 + 1) = 4。
# - i != end，不增加跳数。
#
# 循环结束，返回 2。
# 对应的一条路线：0 → 2 → 4。
#
#
# 六、为什么只检查到倒数第二个下标？
#
# 1. 到达终点就成功，不需要从终点再次起跳。
#    - 终点上的数字，只决定到达终点后还能跳多远。
#    - 它不会影响到达终点所需的跳数。
#
# 2. 到达终点的最后一跳，会在检查前面的位置时被计入。
#
#    例如 nums = [1, 0]：
#    - 检查下标 0，发现能到下标 1。
#    - step 更新成 1，end 更新成 1。
#    - 已经知道 1 跳可以到终点，不需要再检查终点。
#
# 3. 如果遍历终点，可能多算一次。
#
#    例如 nums = [1, 0]：
#    - 处理完下标 0，step = 1，end = 1。
#    - 如果继续检查下标 1，又会触发 i == end。
#    - step 就会错误地变成 2。
#
# 4. 数组只有一个元素时：
#    - range(len(nums) - 1) 就是 range(0)。
#    - 循环不执行，返回 step = 0，符合题意。
#
#
# 七、循环到底怎么结束？为什么结束后能返回答案？
#
# 1. for 循环的结束由 range 决定，与 end、farthest 无关。
#
#    数组长度为 5：
#    - range(len(nums) - 1) 就是 range(4)。
#    - i 依次取 0、1、2、3。
#    - 处理完下标 3，没有下一个 i，循环自然结束。
#
# 2. i == end 不会结束循环。
#    - 它只表示当前这一批候选位置检查完。
#    - 用来增加跳数、更新边界。
#
# 3. 为什么不用等 i 走到终点？
#    - 我们统计的是能覆盖终点的跳数，不是在模拟实际行走。
#    - 当前面的某一批候选位置能跳到终点时，最后一跳就已计入。
#
# 4. 为什么覆盖终点后不会继续增加跳数？
#    - 此时 end >= len(nums) - 1。
#    - 但循环中的 i 最大是 len(nums) - 2。
#    - 因此不会再次触发 i == end。
#
# 5. 为什么循环结束后可以直接返回 step？
#    - 题目保证有解，最终一定能够覆盖终点。
#    - 最后一跳已经在前面的边界更新中被计入。
#    - 后续检查不会再增加跳数，所以最终 step 就是答案。
#
#
# 八、倒数第二个元素为 0 怎么办？
#
# 1. 没关系，不一定要落在倒数第二个位置。
#
#    例如 nums = [2, 0, 0]：
#    - 可以直接从下标 0 跳到终点 2。
#    - 倒数第二个位置为 0，不影响答案。
#
# 2. 循环检查某个位置，不代表实际跳到了那里。
#
# 3. 如果前面也无法跳过这个 0，可能确实无解。
#    - 原题保证有解，因此不会出现无法到达终点的输入。
#
#
# 九、易错点
#
# 1. 错误：farthest 每扩大一次，step 就加 1。
#    - 同一批候选位置可能多次扩大最远距离。
#    - 这些只是不同的落点选择，不代表连续进行了多次跳跃。
#    - 应该在 i == end 时才增加跳数。
#
#    反例：nums = [3, 3, 3, 3, 0, 0, 0]。
#    - 下标 1、2、3 分别把最远距离扩大到 4、5、6。
#    - 但它们都属于第一跳的候选落点。
#    - 最少只需 2 跳：0 → 3 → 6。
#
# 2. 错误：farthest = i + nums[i]。
#    - 可能让最远范围缩小。
#    - 必须使用 max 保留之前的最大值。
#
# 3. 错误：step = 0，却把 end 初始化为 nums[0]。
#    - 在这份写法中，跳 0 次只能到下标 0，所以 end = 0。
#    - end 和 farthest 的含义不同，不能混淆。
#
# 4. 错误：先更新边界，再计算当前位置的跳跃能力。
#    - 当前边界位置也是候选位置，不能遗漏。
#    - 必须先更新 farthest，再判断 i == end。
#
# 5. 错误：认为每次直接跳到最远下标就行。
#    - 更近的位置可能拥有更强的下一跳能力。
#    - 要检查同一范围内的所有候选位置。
#
# 6. 错误：把下标、跳跃长度、跳跃次数混在一起。
#    - nums[i]：最大跳跃长度。
#    - i + nums[i]：最远落点的下标。
#    - step：跳跃次数。
#
#
# 十、如果题目不保证有解
#
# 约定：无法到达终点时返回 -1。
# 可以在 i == end 时检查：当前范围是否还能向右扩展。
#
# 将原来的 if 块改为：
#
# if i == end:
#     if farthest == end:
#         return -1
#     step += 1
#     end = farthest
#
# 原因：
# - 已检查完当前所有可达候选位置。
# - 如果 farthest == end，说明下一跳也无法越过当前边界。
# - 当前边界又不是终点，因为循环不检查终点。
# - 所以无法到达终点，返回 -1。
#
# 例如 nums = [1, 0, 0]：
# - i = 0：step = 1，end = 1。
# - i = 1：farthest 仍然是 1。
# - 此时 i == end，并且 farthest == end，返回 -1。
#
# 注意：
# - 只遍历到倒数第二个下标，不依赖“一定有解”。
# - 不做失败检查、直接返回 step，才依赖“一定有解”。
#
#
# 十一、复杂度
#
# 时间复杂度：O(n)。
# - 每个下标最多检查一次，每次只进行常数次操作。
#
# 额外空间复杂度：O(1)。
# - 只维护固定数量的变量。
#
#
# 十二、快速记忆
#
# 每个位置更新最远距离；
# 走到边界才增加跳数；
# 新边界更新为最远距离；
# 终点不需要再起跳。
#
#
# 十三、英文面试口述
#
# I'll use a greedy approach that expands the reachable range layer by layer.
# I track the jump count, the current boundary, and the farthest reach.
#
# At each index, I update how far I can reach with one more jump.
# When I reach the current boundary, I've checked all candidates in this layer,
# so I increment the jump count and update the boundary.
#
# This gives the minimum number of jumps because I explore the reachable
# positions in order of jump count, similar to BFS.
#
# I stop before the last index because reaching it is enough.
# Since the problem guarantees a solution, I return the jump count.
#
# The time complexity is O(n), and the extra space is O(1).