
# Runtime
# 22ms
# Beats 9.03%of users with Python
# Memory
# Details
# 13.13MB
# Beats 83.34%of users with Python
class Solution(object):
    def tribonacciUtil(self,n,memo):
        i=-1
        while(i<n):
            i+=1
            if(i==0):
                memo[i] = 0
            elif(i==1):
                memo[i]=1
            elif(i==2):
                memo[i]=1
            else:
                memo[i] = memo[i-1]+memo[i-2]+memo[i-3]
                
        return memo[n]
        
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0 for i in range(n+1)]
        return self.tribonacciUtil(n,memo)