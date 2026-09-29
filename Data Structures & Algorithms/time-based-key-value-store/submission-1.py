class TimeMap:
    def __init__(self):
        self.store = defaultdict(list) #defaultdict(list) 会在你用 store[key] 访问不存在
                                    #的 key 时，自动调用 list() 创建一个空列表，并放进字典
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        records = self.store.get(key, [])   #key 存在：返回对应的记录列表。
                                            #key 不存在：返回默认值 []。

        left = 0
        right = len(records) - 1   #列表中tuple的个数 - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if records[mid][0] <= timestamp:
                result = records[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result