class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1 
        # Bucket sort 
        countArray = [[] for _ in range(len(nums)+1)]
        for key, val in freq.items():
            countArray[val].append(key)
        res = []
        for i in range(len(countArray)-1, 0,-1):
            for val in countArray[i]:
                res.append(val)
                if len(res) == k:
                    return res
        # Heap O(klon(n))
        # Bucket Sort O(klon(n))