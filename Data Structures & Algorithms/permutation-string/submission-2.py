class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        mp = defaultdict(int)
        for c in s1:
            mp[c] += 1

        for i in range(len(s1)-1, len(s2)):
            res = True
            char = s2[left:i+1]
            cp = {}
            # print(char)

            for c in char:
                if c in cp:
                    cp[c] +=1 
                else:
                    cp[c] =1 

            for key in mp.keys():
                if key not in cp or mp[key] != cp[key]:
                    # print(cp, mp)

                    res = False
                    break
            if res:
                return True
            left += 1 
        return False