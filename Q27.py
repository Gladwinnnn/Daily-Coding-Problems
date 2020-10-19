# All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". 
# When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        checker = set()
        placeHolder = []
        for i in range(len(s)):
            temp = s[i:i+10]
            if temp not in checker:
                checker.add(temp)
            elif temp in checker and temp not in placeHolder:
                placeHolder.append(temp)
        return placeHolder