class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        horizontal = [max(row) for row in grid]
        vertical = [max(column) for column in zip(*grid)]
        return sum(min(vertical[c], horizontal[r]) - val for r, row in enumerate(grid) for c, val in enumerate(row))
