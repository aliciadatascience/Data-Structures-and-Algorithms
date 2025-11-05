class Solution:
    def lengthofLIS(self, nums: List[int]):
        d = []
        for num in nums:
            # bisect is a module of python
            # bisect_left locate the insertion point for x in d to main sorted order
            import bisect
            i = bisect.bisect_left(d, num)
            if i == len(d):
                d.append(num)
            else:
                d[i] = num
        return len(d)


# o(nlogn) solution with binary search
class Solution:
    def lengthofLIS(self, nums):

        def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while lo <= hi:
                mid = lo + (hi - lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo

        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)
