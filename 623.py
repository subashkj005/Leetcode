"""
623. Add One Row to Tree

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the
given depth depth.

Note that the root node is at depth 1.

The adding rule is:

* Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with
value val as cur's left subtree root and right subtree root.
* current's original left subtree should be the left subtree of the new left subtree root.
* current's original right subtree should be the right subtree of the new right subtree root.
*If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.


"""


# Depth First Approach

class Solution:
    def addRowHelper(self, tree_depth, root, val, depth):
        if not root:
            return None

        if tree_depth == depth - 1:
            left_node = root.left
            right_node = root.right

            root.left = TreeNode(val=val)
            root.right = TreeNode(val=val)

            root.left.left = left_node
            root.right.right = right_node

            return root

        root.left = self.addRowHelper(tree_depth + 1, root.left, val, depth)
        root.right = self.addRowHelper(tree_depth + 1, root.right, val, depth)

        return root

    def addOneRow(self, root, val, depth):
        tree_depth = 1
        if depth == 1:
            new_node = TreeNode(val=val)
            new_node.left = root
            return new_node

        return self.addRowHelper(tree_depth, root, val, depth)
