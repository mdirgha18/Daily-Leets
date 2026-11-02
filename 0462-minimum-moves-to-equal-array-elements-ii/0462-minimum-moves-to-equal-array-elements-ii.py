import numpy as np

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        a = np.array(nums)
        med = np.partition(a, len(a) // 2)[len(a) // 2]
        return int(np.abs(a - med).sum())