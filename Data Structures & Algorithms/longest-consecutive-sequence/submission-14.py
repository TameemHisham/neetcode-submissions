class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        if len(nums) == 0: return res
        sorted_arr = list(sorted(set(nums)))
        print(sorted_arr)
        current_streak = 0 
        for i in range(len(sorted_arr)-1):
            if sorted_arr[i] == sorted_arr[i+1]-1:
                current_streak += 1
                if current_streak > res:
                    res = current_streak
            else:
                current_streak = 0

        return res+1      

