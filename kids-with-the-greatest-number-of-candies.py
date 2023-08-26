# Python solution Runtime Beats 95.84% Memory Beats 88.91%
# Avinilcodes

# Python
# Intuition
# Simple thought just add extraCandies value to each and check with max from list.

# Approach
# Get max of from list and store it in variable and then just map over list checking condition

# Complexity
# Time complexity:
# O(N)

# Space complexity:
# O(1)

# Code
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        mx = max(candies)
        return map(lambda x:(x+extraCandies)>=mx, candies)