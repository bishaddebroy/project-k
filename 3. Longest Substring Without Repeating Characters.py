class Solution:
    # Sliding Window. Time: O(N), Space: O(min(M, N)) where N is the length of the string and M is the size of the charset.
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, length = 0, 0
        dup = set()

        for R in range(len(s)):
            while s[R] in dup:
                dup.remove(s[L])
                L += 1
            dup.add(s[R])
            length = max(length, R - L + 1)
        
        return length