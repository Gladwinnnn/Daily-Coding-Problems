# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
# return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a maximal substring consisting of non-space characters only.

# Input: "Hello World"
# Output: 5

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        length = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                length += 1
            else: 
                return length
        return length