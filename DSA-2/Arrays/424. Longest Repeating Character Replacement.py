class Solution:

    # Sliding Window + HashMap. Time: O(N). Space: O(1).
    # The size of the hashmap is at most 26.
    def characterReplacement(self, s: str, k: int) -> int:
        L, Length = 0, 0
        repeat = {}

        for R in range(len(s)):
            repeat[s[R]] = 1 + repeat.get(s[R], 0)

            while (R - L + 1) - max(repeat.values()) > k:
                repeat[s[L]] -= 1
                L += 1
            
            Length = max(Length, R - L + 1)
        
        return Length
    
    # Sliding Window + HashMap + maxf. Time: O(N). Space: O(1).
    # The size of the hashmap is at most 26.
    def characterReplacement(self, s: str, k: int) -> int:
        L, Length = 0, 0
        repeat = {}
        maxf = 0

        for R in range(len(s)):
            repeat[s[R]] = 1 + repeat.get(s[R], 0)
            maxf = max(maxf, repeat[s[R]])

            while (R - L + 1) - maxf > k:
                repeat[s[L]] -= 1
                L += 1
            
            Length = max(Length, R - L + 1)
        
        return Length
        