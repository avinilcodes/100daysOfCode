# Avinil Bedarkar

# Details
# Solution
# Python
# Runtime
# 25 ms
# Beats
# 32.96%
# Memory
# 13.6 MB
# Beats
# 11.84%

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        da = dict()
        for i in arr:
            if i not in da.keys():
                da[i] = 1
            else:
                da[i] += 1
        dv = da.values()
        if list(sorted(set(dv))) == list(sorted(dv)):
            return True
        return False 