# Python beats 83.93% in runtime and 20.47% in memory
# Avinilcodes
# Intuition
# sum until current element and keep updating max value i.e. altitude

# Approach
# simple keep on updating max altitude and sum

# Complexity
# Time complexity:
# O(N)

# Space complexity:
# O(1)

# Code
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        mx, cur = 0,0
        for i in range(len(gain)):
            cur = cur+gain[i]
            if cur > mx:
                mx = cur
        return mx