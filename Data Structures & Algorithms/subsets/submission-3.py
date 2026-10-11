class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def backtrack(i):
            if i == len(nums):
                result.append(path.copy())
                return
            
            path.append(nums[i])
            backtrack(i+1)

            path.pop() #不是！！path.pop(nums[i])，pop会自动选择
            backtrack(i+1)

        backtrack(0)
        return result

# Python 列表 pop() — 用法讲解
#
# 1. 作用：
#    - 删除列表中的一个元素，并返回被删除的元素。
#    - 会直接修改原列表。
#
# 2. 不传参数：list.pop()
#    - 默认删除最后一个元素。
#
# 3. 传入参数：list.pop(index)
#    - 删除指定下标位置的元素。
#    - 参数是下标，不是要删除的元素值。
#
# 4. 支持负数下标：
#    - pop(-1)：删除最后一个元素，与 pop() 等价。
#    - pop(-2)：删除倒数第二个元素。
#
# 5. 在回溯中的用法：
#    path.append(nums[i])   # 把当前数字加入列表末尾
#    backtrack(i + 1)      # 探索后面的选择
#    path.pop()            # 删除末尾元素，撤销当前选择
#
#    - 更深层的递归会撤销它们各自加入的元素。
#    - 返回当前层时，末尾元素就是当前层加入的 nums[i]。
#    - 因此直接使用 path.pop()，不需要传参数。
#    - 不要写 path.pop(nums[i])，这会把 nums[i] 当作下标。
#
# 6. 如果想按元素值删除：
#    - 使用 list.remove(value)。
#    - remove 删除第一个匹配的元素，不返回被删除的值。
#
#    path = [10, 20, 30]
#    path.remove(20)
#    此时 path == [10, 30]
#
# 7. 注意报错：
#    - 对空列表执行 pop()，会触发 IndexError。
#    - pop(index) 的下标超出范围，也会触发 IndexError。
