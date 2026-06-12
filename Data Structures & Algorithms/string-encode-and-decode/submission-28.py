class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
                return "empty" 
        encoded_string = ""
        for word in range(len(strs)):
            
            for c in strs[word]:
                encoded_string += str(ord(c))+" "
            if word != len(strs)-1:
                encoded_string += ","
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        print(s)
        strs = []
        for current_word in s.split(","):
            word = ""
            for c in current_word.split():
                print(c)
                if c != " ":
                    word += chr(int(c))
            strs.append(word)
        return strs
