https://leetcode.com/problems/first-bad-version/    
class Solution:
    def firstBadVersion(self,n):
        start = 1
        end = n + 1

        while start < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1

        if isBadVersion(start) == True:
            return start
        if isBadVersion(end) == True:
            return end

        return -1

