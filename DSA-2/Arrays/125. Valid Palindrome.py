class Solution:
    # Time Complexity: O(n). Space Complexity: O(n)
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    
    # Time Complexity: O(n). Space Complexity: O(1)
    def isPalindrome2(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
    
    # Alternative using ord()
    def isPalindrome3(self, s: str) -> bool:
        def isAlphaNumeric(c):
            return (ord('a') <= ord(c) <= ord('z') or
                    ord('A') <= ord(c) <= ord('Z') or
                    ord('0') <= ord(c) <= ord('9'))
        
        def toLower(c):
            if ord('A') <= ord(c) <= ord('Z'):
                return chr(ord(c) + 32)
            return c
        
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not isAlphaNumeric(s[left]):
                left += 1
            while left < right and not isAlphaNumeric(s[right]):
                right -= 1
            if toLower(s[left]) != toLower(s[right]):
                return False
            left += 1
            right -= 1
        return True