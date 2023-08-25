# Python solution beats 99.96% in runtime and 82.19% in memory
# Avinilcodes

# Python
# Intuition
# Approach
# check lenth of both words and merge until length of word1 or word2 whichever is less, and then append remaining of either.

# Complexity
# Time complexity:
# O(N)

# Space complexity:
# O(1)

# Code
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        lenWord1 = len(word1)
        lenWord2 = len(word2)
        final = ""
        i = 0
        while(i<lenWord1 and i<lenWord2):
            final+= word1[i]
            final+= word2[i]
            i+=1
        if i < lenWord1:
            final+= word1[i:]
        else:
            final+= word2[i:]
        return final