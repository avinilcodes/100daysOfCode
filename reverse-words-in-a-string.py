# Python solution beats Beats 69.31% in runtime and Beats 22.79% in memory
# Avinilcodes

# Python
# Intuition
# Use functions in python effectively

# Approach
# Complexity
# Time complexity:
# O(N)

# Space complexity:
# O(N)

# Code
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(list(filter(lambda x:x !="", split(rstrip(lstrip(s)), ' ')))))