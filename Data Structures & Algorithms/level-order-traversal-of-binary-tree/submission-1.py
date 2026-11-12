# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        queue = deque([root])
        to_return = []

        while (len(queue) > 0):
            tier = []
            size = len(queue)
            for i in range(size):
                current = queue.popleft()
                if current:
                    tier.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)
            if tier:
                to_return.append(tier)
        return to_return
            
