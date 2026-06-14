class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res, left = 0, head

        def dfs(right):
            nonlocal res, left
            if right.next: dfs(right.next)
            res = max(res, left.val + right.val)
            left = left.next
        
        dfs(head)
        return res