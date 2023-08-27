
# Python solution for O(N) time complexity
# Avinilcodes

# Python
# Intuition
# Place flower where there are no adjacent flowers

# Approach
# check for corner cases and find place flower by checking adjacent places.

# Complexity
# Time complexity:
# O(N)

# Space complexity:
# O(1)

# Code
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        lenFB = len(flowerbed)
        if(lenFB== 1 and n==1 and flowerbed[0]==0):
            return True
        for i in range(0,lenFB-1):
            if n==0:
                return True
            if(i==0 and flowerbed[i]==0 and flowerbed[i+1]==0):
                flowerbed[i] = 1
                n-=1
                continue
            if(i == lenFB-2 and flowerbed[i] == 0 and flowerbed[i+1] == 0):
                flowerbed[i+1] = 1
                n -= 1
                break
            if(flowerbed[i-1] != 1 and flowerbed[i+1] != 1 and flowerbed[i]!=1 ):
                flowerbed[i] = 1
                n -= 1
        if(n==0):
            return True
        else:
            return False