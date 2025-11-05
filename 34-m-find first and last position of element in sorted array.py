https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Solution 1:
class Solution:
    def searchRange(self, nums, target):
        import bisect
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        return [-1,-1] if l == r else [l, r-1]


# Solution 2:
class Solution:
    def searchRange(self, nums, target):
        def binarySearchLeft(A,x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = left + (right - left)//2
                if x > A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = left + (right - left)//2
                if x>= A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]
