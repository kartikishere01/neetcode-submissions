from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        t = len(numbers) - 1
        i = 0
        while i<t:
            if numbers[i] + numbers[t] > target:
                t = t - 1
            elif numbers[i] + numbers[t] < target :
                i = i + 1
            else :
                return [i+1,t+1]

