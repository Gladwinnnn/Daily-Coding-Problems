# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# Input: digits = [0]
# Output: [1]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = ""
        for elements in digits:
            digits_str += str(elements)
        digits_int = int(digits_str)
        digits_int += 1
        digits_str = str(digits_int)
        result = []
        for elements in digits_str:
            result.append(int(elements))
        return result