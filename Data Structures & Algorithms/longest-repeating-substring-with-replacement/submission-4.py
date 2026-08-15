class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = defaultdict(int)
        res = 0
        left = 0 
        maxFreq = 0
        for right in range(len(s)):
            table[s[right]] += 1
            maxFreq = max(maxFreq, table[s[right]])
            while (right-left+1)-maxFreq > k:
                table[s[left]] -= 1
                left +=1 
            res = max(res, right - left + 1)

        return res


                    