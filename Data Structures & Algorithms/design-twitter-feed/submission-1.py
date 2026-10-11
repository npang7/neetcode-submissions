class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time,tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        heap = []
        users = self.following[userId] | {userId}

        # 1.建立初始miniHeap：用每个用户最新的一条
        for author in users:
            posts = self.tweets[author]

            if posts:
                index = len(posts) - 1
                timestamp, tweet_id = posts[index] #该用户的最新一条

                heap.append([
                    -timestamp,
                    tweet_id,
                    author,
                    index
                ])
        heapq.heapify(heap)

        #2.不断更新miniHeap和result
        # 最多取出十条推文
        while heap and len(result) < 10:
            negative_time, tweet_id, author, index = heapq.heappop(heap)
            result.append(tweet_id)

            # 如果该作者还有更旧的推文，放入上一条
            if index > 0:
                index -= 1
                timestamp, tweet_id = self.tweets[author][index]

                heapq.heappush(heap, [
                    -timestamp,
                    tweet_id,
                    author,
                    index
                ])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId) #'set' object has no attribute 'append'

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
