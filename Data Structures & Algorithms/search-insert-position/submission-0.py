class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = 0
        while right >= left:
            mid = (right+left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1 
        if nums[mid] > target:
            return mid
        return mid + 1