class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix[0])
        for n in matrix:
            if n[-1] == target:
                return True
            if n[-1] > target:
                while left <= right:
                    mid = (left + right) //2 
                    if target == n[mid]:
                        return True
                    if n[mid] > target:
                        right = mid -1 
                    else:
                        left = mid + 1
        return False