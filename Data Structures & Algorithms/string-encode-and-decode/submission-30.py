class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
                return "empty" 
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word))+"#"+word
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        print(s)
        strs = []
        pointer = 0
        current_length = ""
        while pointer < len(s):
            if s[pointer] == "#":
                strs.append(s[pointer+1:pointer+1+int(current_length)])
                pointer += 1+int(current_length)
                current_length = ""

            else:
                current_length += s[pointer]
                pointer += 1
        return strs
