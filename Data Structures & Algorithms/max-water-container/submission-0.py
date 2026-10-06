class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        

        l = len(heights)-1
        res = 0

        while i<l :
            area = (l-i)*min(heights[i],heights[l])
            res = max(res,area)

            if heights[i]<heights[l]:
                i = i + 1
            else:
                l = l - 1

        return res   


