# Runtime
# 374ms
# Beats 44.57%of users with Python
# Memory
# 16.75MB
# Beats 94.14%of users with Python

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
        return sum(self.nums[left:right+1])
        


# YourN umArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)