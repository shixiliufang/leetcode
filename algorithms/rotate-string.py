class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == '' and B == '':
            return True
        return any(A[ch:] + A[:ch] == B for ch in range(len(A)))
