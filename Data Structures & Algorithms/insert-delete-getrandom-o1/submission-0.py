import random
class RandomizedSet:

    def __init__(self):
        self.positions = {} #positions[val] = index
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False
        self.nums.append(val)
        index = len(self.nums)-1
        self.positions[val] = index
        return True

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False
        last_index = len(self.nums)-1
        index = self.positions[val]
        self.nums[index] = self.nums[last_index]
        self.positions[self.nums[last_index]] = index
        self.nums.pop()
        del self.positions[val]


    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()