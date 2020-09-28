# Given a 32-bit signed integer, reverse digits of an integer.

# Input: 123
# Output: 321

# Input: -123
# Output: -321

# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            placeHolder = "-"
        else:
            placeHolder = ""
        number = str(abs(x))
        for i in range(len(number)-1,-1,-1):
            placeHolder += number[i]
        result = int(placeHolder)
        if result > 2 ** 31 - 1 or result < -2 ** 31:
            return 0
        else:
            return result