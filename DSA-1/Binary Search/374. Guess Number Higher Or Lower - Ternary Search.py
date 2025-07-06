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
            m1 = l + (r-l)//2
            m2 = r - (r-l)//2

            g1 = guess(m1)
            g2 = guess(m2)

            if g1 == 0:
                return m1
            elif g2 == 0:
                return m2
            elif g1 + g2 == 0:
                l = m1 + 1
                r = m2 - 1
            elif g1 == -1:
                r = m1 - 1
            else:
                l = m2 + 1
        