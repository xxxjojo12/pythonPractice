class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
	        return False
        return str(x) == str(x)[::-1]


a = Solution()
print(a.isPalindrome(121))