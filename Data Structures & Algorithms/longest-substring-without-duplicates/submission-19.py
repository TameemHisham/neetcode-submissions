class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}
        left = 0
        res = 0
        for right in range(len(s)):
            if s[right] in index:
                left = max(left, index[s[right]] + 1)
            length = right-left+1
            res = max(length,res)
            index[s[right]] = right
        return res 

