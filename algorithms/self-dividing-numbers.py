class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def self_dividing(n):
            for digit in str(n):
                if digit == '0' or n % int(digit) != 0:
                    return False
            return True

        answer = []
        for num in range(left, right + 1):
            if self_dividing(num):
                answer.append(num)
        return answer
