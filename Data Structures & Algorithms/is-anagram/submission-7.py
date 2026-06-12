class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = defaultdict(int)
        for c in s:
            frequency[c] += 1
        for c in t:
            frequency[c] -= 1
        for key in frequency.keys():
            if frequency[key] != 0:
                return False
        return True