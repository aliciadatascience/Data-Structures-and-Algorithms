
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]):
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        lookup = set()
        for i in nums1:
            lookup.add(i)

        result = []
        for i in nums2:
            if i in lookup:
                result.append(i)
                lookup.discard(i)
        return result

    # another solution
    def intersection(self, nums1: List[int], nums2: List[int]):
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)
