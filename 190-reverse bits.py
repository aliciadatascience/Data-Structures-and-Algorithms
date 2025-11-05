# do logic "and"(&) to figure out what the bit is
# do bit shift operation(<<) to move to the left
# shift to the right by i(n>>i)
# shift to the left by i(n << 31-i)

# time complexity O(1) ('cause be guaranteed that there's going to be 32 bits
# space complexity O(1)

class Solution:
    def reverseBits(self, n:int):
        res = 0

        for i in range(32):
            bit = (n>>i) & 1
            res = res | (bit << (31-i))
        return res
