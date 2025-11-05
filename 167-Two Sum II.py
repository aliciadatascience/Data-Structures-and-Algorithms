https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# 167
class Solution(object):
    def twoSum(self, numbers, target):
        start = 0
        end = len(numbers)-1
        sum = 0
       
    
        while start != end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start+1, end+1]
            

