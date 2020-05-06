# https://leetcode.com/problems/shortest-palindrome/
class Solution:

    def isPalindrome(self, s):
            return s == s[::-1]

    def shortestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s) == True:
            return s

        for x in range(1, len(s)):
            if self.isPalindrome(s[0:-x]) == True:
                s = s[-x::][::-1] + s
                break
        return s
        
