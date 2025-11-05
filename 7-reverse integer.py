class Solution:
    def reverse(self, x):
        sign = [1, -1][x < 0]
        rev_int = sign * int(str(abs(x))[::-1])
        return rev_int if -(2**31)-1 < rev_int < 2**31 else 0


