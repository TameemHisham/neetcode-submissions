class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequency = defaultdict(list)
        for word in strs:
            sorted_letters = "".join(sorted(word))
            frequency[sorted_letters].append(word)
        return list(frequency.values())