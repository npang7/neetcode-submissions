import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        # 全局发布顺序，数字越大表示越新
        self.time = 0

        # 用户ID → 该用户的推文列表
        # 每条推文保存 [发布时间, 推文ID]
        self.tweets = defaultdict(list)

        # 用户ID → 该用户关注的用户集合
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 新推文追加在列表末尾
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        heap = []

        # 动态包含关注用户以及用户自己
        users = self.following[userId] | {userId}

        # 每个相关用户先提供一条最新推文
        for author in users:
            posts = self.tweets[author]

            if posts:
                index = len(posts) - 1
                timestamp, tweet_id = posts[index]

                heap.append([
                    -timestamp,
                    tweet_id,
                    author,
                    index
                ])

        heapq.heapify(heap)

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
        # 将被关注者加入关注集合
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 如果存在，就删除；不存在也不会报错
        self.following[followerId].discard(followeeId)


        