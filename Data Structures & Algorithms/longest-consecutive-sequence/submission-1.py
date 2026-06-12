class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(list(set(nums)))
        arr=[1 for _ in nums]
        j = 0
        print(nums)
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                print(nums[i])
                arr[j] += 1
            else:
                j+=1
        return max(arr)

