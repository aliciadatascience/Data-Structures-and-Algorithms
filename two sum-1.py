class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

# since we know the target, as long as we maintain a record of all previous values,
# we can compare the current value to the previous records.

