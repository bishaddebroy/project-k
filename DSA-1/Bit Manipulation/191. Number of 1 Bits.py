class Solution:
    # Brian Kernighan’s Algorithm -> Count set bits
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (1 << i) & n:
                res += 1
        return res

    # Brian Kernighan’s Algorithm -> Alternative
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1 if n & 1 else 0
            n = n >> 1
        return res

    # Brian Kernighan’s Algorithm -> Most Efficient
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res

    # Pythonic Way -> Using built-in functions
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    