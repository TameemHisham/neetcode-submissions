class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {val: i for i, val in enumerate(nums)}
        for j in range(len(nums)):
            complement = target-nums[j]
            if complement in complements and j !=complements[complement]:
                return [j,complements[complement]]
        return []