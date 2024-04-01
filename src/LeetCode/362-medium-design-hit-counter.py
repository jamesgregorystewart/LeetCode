class HitCounter:

    def __init__(self):
        self.hits = []
        self.last_hit = None

    def hit(self, timestamp: int) -> None:
        if not self.last_hit or self.last_hit[0] != timestamp:
            hit = (timestamp, 1)
            self.last_hit = hit
            self.hits.append(hit)
        else:
            hit = self.hits[-1]
            hit = (timestamp, hit[1] + 1)
            self.hits[-1] = hit

    def getHits(self, timestamp: int) -> int:
        left, right = 0, len(self.hits) - 1
        while left < right:
            mid = (left + right) // 2
            if self.hits[mid][0] <= (timestamp - 300):
                left = mid + 1
            elif self.hits[right][0] > (timestamp - 300):
                right = mid
        if left < len(self.hits) and self.hits[left][0] <= (timestamp - 300):
            left += 1
        total_hits = 0
        while left < len(self.hits):
            total_hits += self.hits[left][1]
            left += 1
        return total_hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
