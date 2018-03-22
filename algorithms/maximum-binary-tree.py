class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        maxnum = max(nums)
        maxindex = nums.index(maxnum)
        root = TreeNode(maxnum)
        root.left = self.constructMaximumBinaryTree(nums[0:maxindex])
        root.right = self.constructMaximumBinaryTree(nums[maxindex + 1:])
        return root
