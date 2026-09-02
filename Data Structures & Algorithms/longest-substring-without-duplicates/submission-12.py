class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} 
        left = 0
        res = 0
        for i, c in enumerate(s):
            if c in mp:
                left = max(mp[c] + 1, left)
                # left = mp[c] + 1
            mp[c] = i
            res =  max(i-left+1, res) 
        return res
                


