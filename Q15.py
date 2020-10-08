# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

# 0 <= i, j < nums.length
# i != j
# |nums[i] - nums[j]| == k
# Notice that |val| denotes the absolute value of val.

# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.

# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).

# Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
# Output: 2

# Input: nums = [-1,-2,-3], k = 1
# Output: 2

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        placeHolder = []
        result = []
        
        while len(nums) > 0:
            add = nums[0] + k
            sub = nums[0] - k
            element = nums[0]
            nums.pop(0)
            
            if add in nums and (add+element) not in result:
                placeHolder.append((element,add))
                result.append(add+element)
            if sub in nums and (sub+element) not in result:
                placeHolder.append((element,sub))
                result.append(sub+element)

        return len(placeHolder)