__author__ = 'garfield'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)


def print_root(root):
    if root.left:
        print_root(root.left)
    print root.val
    if root.right:
        print_root(root.right)
if __name__ == '__main__':
    root = TreeNode(2)
    left = TreeNode(3)
    left_2 = TreeNode(4)
    left_3 = TreeNode(5)
    right = TreeNode(6)
    right_2 = TreeNode(7)
    right_3 = TreeNode(8)
    root.left = left
    root.right = right
    left.left = left_2
    left.right = right_2
    right.left = left_3
    right.right = right_3
    print_root(root)
    Solution().invertTree(root)
    print_root(root)