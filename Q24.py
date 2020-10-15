# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # """
        # Do not return anything, modify nums in-place instead.
        # """
        placeHolder = []
        if len(nums) == 1:
            nums = nums
        elif k > len(nums):
            index = abs(len(nums) - k)
            for i in range(index,len(nums)):
                placeHolder.append(nums[0])
                nums.pop(0)
            for elements in placeHolder:
                nums.append(elements)
        else:
            for i in range(k,len(nums)):
                placeHolder.append(nums[0])
                nums.pop(0)
            for elements in placeHolder:
                nums.append(elements)