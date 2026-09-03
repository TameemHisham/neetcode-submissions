class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            left, right = i+1 , len(nums)-1
            while right > left:
                val = nums[left] + nums[right] + nums[i] 
                if val > 0:
                    right -= 1
                elif val < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left] , nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
            
        return answer