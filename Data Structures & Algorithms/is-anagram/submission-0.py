class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dic = {}
        t_dic = {}
        
        for char in s:
            s_dic[char] = s_dic.get(char, 0) + 1
        for char in t:
            t_dic[char] = t_dic.get(char, 0) + 1
        
        return s_dic == t_dic