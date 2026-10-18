import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)   # userId -> list of (time, tweetId)
        self.following = defaultdict(set) # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        # include user's own tweets
        for t in self.tweets[userId]:
            heapq.heappush(heap, t)
        # include followees' tweets
        for followee in self.following[userId]:
            for t in self.tweets[followee]:
                heapq.heappush(heap, t)
        # get 10 most recent
        return [tweetId for _, tweetId in heapq.nlargest(10, heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
