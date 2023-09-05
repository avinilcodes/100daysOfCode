# Runtime
# 12ms
# Beats 78.76%of users with Python
# Memory
# Details
# 13.25MB
# Beats 87.69%of users with Python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        C={'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ans=[''] if digits else []
        for d in digits: 
            ans=[x+y for x in ans for y in C[d]]
        return ans