class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        keys = frequency.keys()
        max_values = []
        print(frequency)
        for _ in range(k):
            maxKey = max(frequency, key=frequency.get)
            print(maxKey, frequency[maxKey])
            max_values.append(maxKey)
            frequency[maxKey] = -1
        return max_values
            