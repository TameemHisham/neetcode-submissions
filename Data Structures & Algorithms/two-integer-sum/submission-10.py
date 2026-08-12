class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {val: i for i, val in enumerate(nums)}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in mp and mp[complement] != i:
                return [i, mp[complement]]
        return []
        
            

