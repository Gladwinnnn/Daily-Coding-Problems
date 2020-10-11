# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Input: s = "bcabc"
# Output: "abc"

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        placeHolder = []
        for elements in s:
            if elements not in placeHolder:
                placeHolder.append(elements)
        placeHolder = merge_sort(placeHolder)
        result = ""
        for elements in placeHolder:
            result += elements
        return result
                
def merge_sort(dummy):
    if len(dummy) > 1:
        half = len(dummy)//2
        left = merge_sort(dummy[:half])
        right = merge_sort(dummy[half:])

        values = []

        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                values.append(right[0])
                right.pop(0)
            elif right[0] > left[0]:
                values.append(left[0])
                left.pop(0)
        for elements in left:
            values.append(elements)
        for elements in right:
            values.append(elements)
        return values
    return dummy