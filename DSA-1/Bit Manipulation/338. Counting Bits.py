class Solution:
    # Count using Brian Kernighan’s Algorithm -> Time: O(n log n) Space: O(1)
    def countBits(self, n: int) -> List[int]:
        res = []

        for num in range(n+1):
            one = 0
            for i in range(32):
                if num & (1 << i):
                    one += 1
            res.append(one)
        
        return res

    # Count using Brian Kernighan’s Algorithm -> Alternative
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)

        for i in range(n+1):
            num = i
            while num > 0:
                res[i] += 1
                num &= (num-1)
            
        return res

    # Pythonic Way -> Using built-in functions
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n+1)]

    # Count using Dynamic Programming -> Time: O(n) Space: O(n). Remove Leftmost Bit + that bit.
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

    # Count using DP -> Time: O(n) Space: O(n). Relation: dp[i] = dp[i // 2] + (i % 2). Remove Rightmost Bit + that bit.
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)

        for i in range(1, n+1):
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp