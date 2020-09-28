Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Input: s = ""
Output: 0


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        result = []
        for i in range(len(s)):
            placeHolder = ""
            for j in range(i,len(s)):
                if s[j] not in placeHolder:
                    placeHolder += s[j]
                else:
                    break
            result.append(len(placeHolder))
        result.sort(reverse=True)
        return result[0]