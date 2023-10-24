from typing import List, Dict, Set
from collections import namedtuple
import heapq



Tweet = namedtuple("Tweet", ["tweetId", "userId"]) 

class Twitter:

    def __init__(self):
        self.followees : Dict[int, Set[int]] = {}
        self.tweets : List[Tweet] = []


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followees:
            self.followees[userId] = set([userId])
        self.tweets.append(Tweet(tweetId, userId))


    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followees[userId] if userId in self.followees else set([userId])
        res = []
        for tweet in self.tweets[::-1]:
            if len(res) == 10:
                break
            if tweet.userId in users:
                res.append(tweet.tweetId)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followees:
            self.followees[followerId] = set([followerId, followeeId])
        else:
            self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees:
            self.followees[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
twitter = Twitter()
twitter.postTweet(1, 5) # User 1 posts a new tweet (id = 5).
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2)    # User 1 follows user 2.
twitter.postTweet(2, 6) # User 2 posts a new tweet (id = 6).
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2)  # User 1 unfollows user 2.
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
