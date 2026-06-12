class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ptr1 = 0
        ptr2 = 0
        val = 1
        length = len(nums)
        vals = [0 for _ in range(length)]
        while ptr1 < length:
            if ptr1 != ptr2:
                val *= nums[ptr2]
            ptr2 += 1
            if ptr2 == length:
                vals[ptr1] = val
                ptr1+=1
                ptr2 = 0
                val = 1
        return vals
            
            
