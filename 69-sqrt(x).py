# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 1, x//2
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x/mid:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1





    # solution 1: import math
    def mySqrt(self, x: int):
        import math
        return int(math.sqrt(x))

    # solution: exponent
    def mySqrt(self, x: int):
        return int(x**(1/2))
