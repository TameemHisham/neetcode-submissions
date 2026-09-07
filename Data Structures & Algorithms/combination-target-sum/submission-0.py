class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        currentCombination = []
        def dfs(i, total):
            if total == target:
                result.append(currentCombination.copy())
                return
            if i >= len(nums) or total > target:
                return
            # Take nums[i]
            currentCombination.append(nums[i])
            dfs(i, total + nums[i])  # Repeat the same number
            currentCombination.pop()
            # Skip nums[i]
            dfs(i + 1, total)        # Move to the next number

        dfs(0, 0)
        return result