# (locked)
# time-complexity:o(N)
# space-complexity:o(N)

# iterate from right to left
class Solution:
    def findBuilding(self, heights:List[int]):
        max = float('-inf')
        res = []

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max:
                res.append(i)
                max = heights[i]
        return reversed(res)

# iterate from left to right
class Solution:
    def findBuilding(self, heights:List[int]):
        max = float('-inf')
        res = []

        for i in range(len(heights)):
            res.append(i)
            if heights[i] >= max:
                res = []
                res.append(i)
                max = heights[i]
            else:
                last_res_idx_value = heights[res[len(res) - 1]]
                for j in range(len(res) -2, -1, -1):
                    if last_res_idx_value >= heights[res[j]]:
                        res.pop(j)
        return res



