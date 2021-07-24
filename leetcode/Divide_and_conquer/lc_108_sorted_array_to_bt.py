from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertToBT(self, nums: List[int], left: int, right: int) -> TreeNode:

        if left > right:
            return None

        mid = (int)(left + (right - left) / 2)
        currentNode = TreeNode(nums[mid])
        currentNode.left = self.convertToBT(nums, left, mid - 1)
        currentNode.right = self.convertToBT(nums, mid + 1, right)
        return currentNode

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return
        return self.convertToBT(nums, 0, len(nums) - 1)