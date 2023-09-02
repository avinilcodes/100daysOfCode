# [Python] beats 75.19% in runtime and 61.64% in memory
# Avinilcodes
# Python
# Intuition
# hash table for both arrays and then set difference

# Approach
# hash table for both arrays and then set difference

# Complexity
# Time complexity:
# O(M+N)

# Space complexity:
# O(M+N)

# Code
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        l1 = dict()
        l2 = dict()
        for i in nums1:
            l1[i] = 1
        for i in nums2:
            l2[i] = 1
        return [list(set(l1)-set(l2)), list(set(l2)-set(l1))]