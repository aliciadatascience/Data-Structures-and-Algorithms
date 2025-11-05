# https://leetcode.com/problems/binary-search/


class Solution:
    def search(self, nums: list[int], target: int):
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
        return -1
