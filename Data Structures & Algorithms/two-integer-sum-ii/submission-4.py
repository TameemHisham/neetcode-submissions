class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index2 = 1 
        index1 = 0
        while index2 < len(numbers):
            index1 = 0
            while index1 < index2:
                if numbers[index1]+numbers[index2] == target:
                    return [index1+1, index2+1]
                index1 += 1
            index2 += 1 

        # return [index1+1, index2+1]
