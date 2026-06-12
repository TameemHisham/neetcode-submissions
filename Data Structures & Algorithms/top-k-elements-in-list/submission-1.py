class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        vals = []
        for n , count in counter.items():
            vals.append([count, n])
        vals.sort(reverse=True)
        res = []
        for i in vals[:k]:
            res.append(i[1])
        return res
