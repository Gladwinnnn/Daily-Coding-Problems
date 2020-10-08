# Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

# The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

# For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

# Input: 5
# Output: 2
# Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

# Input: 7
# Output: 0
# Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

# Input: 10
# Output: 5
# Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = ""
        flipped = ""
        complimentary = ""
        base10 = 0
        
        if N == 0:
            return 1
        
        while N != 0:
            binary += str(N%2)
            N = N//2
            
        for i in range(len(binary)-1,-1,-1):
            flipped += binary[i]
            
        for elements in flipped:
            if elements == '1':
                complimentary += '0'
            elif elements == '0':
                complimentary += '1'

        power = 1
        for i in range(len(complimentary)-1,-1,-1):
            base10 += int(complimentary[i]) * power
            power *= 2
            
        return base10