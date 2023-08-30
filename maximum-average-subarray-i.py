class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        cur = mx = sum(nums[0:k])

        for i in range(len(nums)-k):
            cur += nums[i+k] - nums[i]
            mx = max(cur, mx)
        return mx/float(k)