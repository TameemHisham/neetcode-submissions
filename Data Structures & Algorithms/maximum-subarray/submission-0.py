class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        left = 0
        for i, n in enumerate(nums):
            # If the currentSum is Negative then ingore it 
            curSum = max(curSum, 0)
            # Add the current Element 
            curSum += n
            # check if the current sum > max
            maxSum = max(curSum , maxSum)

        return maxSum        

