class Solution(object):
    def minOperations(self, nums, k):
        return sum(nums) % k
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        