class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for t in range(len(nums)):
            for i in range(t + 1, len(nums)):
                if nums[t] + nums[i] == target:
                    return [t, i]