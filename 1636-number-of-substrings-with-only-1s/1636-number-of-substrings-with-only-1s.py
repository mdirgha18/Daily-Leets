class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        total = 0
        mod = 1000000007
        for a in s:
            if a == '1':
                cnt += 1
            else:
                cnt = 0
            total = (total + cnt) % mod
        return total
        