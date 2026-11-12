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
        if root == None:
            return to_return

        while (len(queue) > 0):
            tier = []
            size = len(queue)
            for i in range(size):
                current = queue.popleft()
                if current != None:
                    tier.append(current.val)
                    if current.left != None:
                        queue.append(current.left)
                    if current.right != None:
                        queue.append(current.right)
            to_return.append(tier)
        return to_return
            
