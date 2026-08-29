class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            left, right = 0, len(nums)-1
            if nums[right] < target:
                continue
            if nums[left] > target:
                continue
            while right >= left:
                mid = (left+right) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] > target:
                    right = mid -1 
                else:
                    left = mid +1 
        return False