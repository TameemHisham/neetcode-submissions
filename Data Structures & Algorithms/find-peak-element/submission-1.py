class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0 , len(nums)-1
        while right >= left:
            mid= (left+right) // 2
            outside_right = mid == len(nums) - 1
            outside_left = mid == 0
            if  (outside_right or nums[mid+1] < nums[mid]) and (outside_left or nums[mid-1] < nums[mid])  :
                return mid
            if nums[mid+1] > nums[mid]:
                left = mid +1 
            else:
                right = mid - 1
