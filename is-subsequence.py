# Runtime
# Details
# 24ms
# Beats 13.12%of users with Python
# Memory
# Details
# 13.30MB
# Beats 83.90%of users with Python
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dp = [0 for p in s]
        ls = len(s)
        i = 0
        j = 0
        while(i<ls and j<len(t)):
            if s[i] == t[j]:
                dp[i] = 1
                i+=1
                j+=1
            else:
                j+=1
        if sum(dp) == ls:
            return True
        return False