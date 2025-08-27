class Solution:
    # Reverse bits by constructing the binary string and then reversing it
    def reverseBits(self, n: int) -> int:
        binary = ""

        for i in range(32):
            if n & (1 << i):
                binary += "1"
            else:
                binary += "0"
        
        res = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res |= (1 << i)
        
        return res

    # Reverse bits using bit manipulation
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1 # or bit = 1 if n & (1 << i) else 0
            res += (bit << (31 - i)) # or res |= (bit << (31 - i))
        
        return res