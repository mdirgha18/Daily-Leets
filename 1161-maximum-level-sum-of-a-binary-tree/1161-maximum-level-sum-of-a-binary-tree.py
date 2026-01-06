class Solution:
    def maxLevelSum(self, root):
        queue = deque()
        queue.append(root)
        max_sum = float('-inf')
        level_count = 0
        smallest_level = 0

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                currNode = queue.popleft()

                level_sum += currNode.val

                if currNode.left:
                    queue.append(currNode.left)

                if currNode.right:
                    queue.append(currNode.right)

            level_count += 1

            if level_sum > max_sum:
                max_sum = level_sum
                smallest_level = level_count

        return smallest_level