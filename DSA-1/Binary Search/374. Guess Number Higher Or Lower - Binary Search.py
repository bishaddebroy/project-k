# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while True:
            m = l + (r-l)//2
            g = guess(m)
            if g == -1:
                r = m - 1
            elif g == 1:
                l = m + 1
            else:
                return m
        