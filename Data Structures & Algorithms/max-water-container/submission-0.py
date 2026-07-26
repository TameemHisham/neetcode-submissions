class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        area = -1
        while left < len(heights): 
            currArea= (right-left) * min(heights[left], heights[right])
            if currArea > area:
                area = currArea
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return area
