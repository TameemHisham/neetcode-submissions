
class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)  # userId: [(timestamp, tweetId)]
        self.timestamp = 0
        self.following = defaultdict(set)  # userId: set of followees


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        users = self.following[userId] | {userId}

        for user in users:
            for timestamp, tweetId in self.tweets[user]:
                res.append((timestamp, tweetId))

        heapq.heapify(res)
        return [
            tweetId
            for timestamp, tweetId in heapq.nlargest(10, res)
        ]
            


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
