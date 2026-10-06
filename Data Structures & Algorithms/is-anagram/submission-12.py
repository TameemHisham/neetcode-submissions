class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frq = defaultdict(int)
        for c in s:
            frq[c] += 1
        for c in t:
            frq[c] -= 1
        for val in frq.values():
            if val != 0:
                return False
        return True

        