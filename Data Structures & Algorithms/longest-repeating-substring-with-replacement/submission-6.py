class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxFreq = 0 
        freq = defaultdict(int)
        left = 0
        for right, value in enumerate(s):
            freq[value] += 1
            maxFreq = max(freq[value], maxFreq)
            while (right-left+1)-maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            res = max(right-left+1, res)
        return res