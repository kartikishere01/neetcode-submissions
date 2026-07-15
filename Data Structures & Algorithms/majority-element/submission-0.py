class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t={}
        for i in nums:
            if i in t:
                t[i]+=1
            else:
                t[i]=1
       
        for key in t:
            if t[key] > len(nums)//2 :
               return key