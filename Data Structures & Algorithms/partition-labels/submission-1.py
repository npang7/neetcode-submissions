class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        start = 0
        end = 0
        res = []
        for i,char in enumerate(s):
            last[char] = i
        for i, char in enumerate(s):
            end = max(end, last[char])
            if i == end:
                res.append(end-start+1)
                start = end + 1

        return res

# Partition Labels（划分字母区间）
#
# 1. 目标：划分出尽可能多的连续片段，同一字母不能出现在不同片段中。
#
# 2. 先遍历字符串，用 last 记录每个字母最后出现的下标。
#    - 下标递增，直接覆盖即可，不需要 max。
#
# 3. 再次遍历，维护当前片段的起点 start 和右边界 end。
#    - end = max(end, last[char])。
#    - 当前片段必须包含其中所有字母的最后一次出现。
#
# 4. 当 i == end，当前片段中的字母不会再出现在后面，可以切分。
#    - 长度为 end - start + 1，包含两端。
#    - 下一段起点为 end + 1。
#    - 不需要重置 end，下一轮会自动更新。
#
# 5. 贪心：一旦可以安全切分就立即切，得到最多的片段。
#
# 易错点：
# - 长度不是 end + 1，要减去当前片段的起点。
# - 更新 end 必须用 max，不能让边界缩小。
# - 先更新 end，再判断能否切分。
#
# 时间：O(n)。
# 额外空间：O(1)，不计返回结果，last 最多保存 26 个小写字母。
#
# 快速记忆：记录最后位置，扩展当前边界，走到边界就切分。


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, char in enumerate(s):
            last[char] = i

        start = 0
        end = 0
        res = []

        for i, char in enumerate(s):
            end = max(end, last[char])

            if i == end:
                res.append(end - start + 1)
                start = end + 1

        return res


# English:
# I first record the last index of each character.
# Then I scan the string and extend the current partition's boundary
# to include the last occurrence of every character I encounter.
# When the current index reaches the boundary, I record the partition's
# length and move the start to the next index.
# Cutting as soon as it's safe gives the maximum number of partitions.
# The time complexity is O(n), and the extra space is O(1),
# excluding the output, because there are only 26 lowercase letters.