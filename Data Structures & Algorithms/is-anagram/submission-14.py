class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        need = defaultdict(int)
        want = defaultdict(int)
        for i in range(len(s)):
            need[s[i]] += 1 
            want[t[i]] += 1
        return want == need
