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

# I use a dictionary that maps each key to a list of timestamp-value pairs.
# For set, I append the new pair to the key’s list. Since the timestamps are strictly increasing, each list stays sorted by timestamp.
# For get, I use binary search to find the latest record whose timestamp is less than or equal to the query timestamp.
# If the middle record’s timestamp is at most the query timestamp, I save its value as a candidate answer and search to the right for a more recent valid record. Otherwise, the record is too late, so I search to the left.
# I return the candidate answer after the search. If the key doesn’t exist or no record satisfies the condition, I return an empty string.
# set takes amortized constant time. get takes O(log m) time, where m is the number of records for that key. The total space is O(N), where N is the total number of stored records.

