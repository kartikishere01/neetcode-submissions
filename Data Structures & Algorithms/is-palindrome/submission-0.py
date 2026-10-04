class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        
        sn=""
        for c in s:
            if c.isalnum():
                sn += c.lower()
        right = len(sn) - 1
        while left < right :
            if sn[left]==sn[right]:
                left = left + 1
                right = right - 1 
            else:
                return False
        return True

                

        