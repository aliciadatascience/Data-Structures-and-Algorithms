https://leetcode.com/problems/search-a-2d-matrix/
# Solution 1: complexity:O(log(mn))
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) //2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


# Solution 2: complexity:O(log(mn))
class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        if m ==0:
            return False
        if m == 0:
            return False
        temp = []
        for i in range(m):
            temp.append(matrix[i][0])
        ind = bisect.bisect_left(temp, target)
        if ind == len(temp):
            ind = ind - 1
        if target < matrix[ind][0]:
            ind = ind - 1

        ind2 = bisect.bisect_left(matrix[ind], target)
        if ind2 == n:
            return False
        return matrix[ind][ind2] == target
