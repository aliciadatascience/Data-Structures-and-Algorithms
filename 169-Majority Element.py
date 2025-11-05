# https://leetcode.com/problems/majority-element/
# sorting
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

# time complexity: o(nlogn)
# space complexity: o(1) or o(n)


## HashMap
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
# Time complexity: O(n)
# Space complexity: O(n)
