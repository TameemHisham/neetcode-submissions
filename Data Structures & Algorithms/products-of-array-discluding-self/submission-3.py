class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            mul = nums[:i] + nums[i+1:]
            val = 1
            for num in mul:
                val *= num
            arr.append(val)
        return arr