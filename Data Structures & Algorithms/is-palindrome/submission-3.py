class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = s.lower().split()
        for i in range(len(arr)):
            if not arr[i].isalnum():
                if len(arr[i]) == 1:
                    arr.pop(i)
                else:
                    temp = ""
                    for c in arr[i]:
                        if c.isalnum():
                            temp+=c
                    arr[i]=temp
        print(arr)
        string = "".join(arr)
        print(string)
        print(string[::-1])
        return string == string[::-1]