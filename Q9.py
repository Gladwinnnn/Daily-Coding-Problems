# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Input: 121
# Output: true

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            temp = str(x)
            placeHolder = ""
            for i in range(len(temp)-1,-1,-1):
                placeHolder += temp[i]
            result = int(placeHolder)
            return result == x
        