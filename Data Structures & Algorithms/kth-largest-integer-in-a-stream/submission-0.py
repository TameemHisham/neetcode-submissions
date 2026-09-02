class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        extra = 0
        for num in self.nums:
            if num < val:
                extra += 1
            else:
                break
        self.nums = [*self.nums[:extra],val,*self.nums[extra:]]
        # print(self.nums, extra)
        return self.nums[-self.k]
