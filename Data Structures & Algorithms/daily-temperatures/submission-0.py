class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pairs [temp, index]
        output = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                output[stackIndex] = index-stackIndex
            stack.append([temp, index])

        return output