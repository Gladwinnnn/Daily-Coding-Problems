# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.

# Given nums = [0,0,1,1,1,2,2,3,3,4],

# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

# It doesn't matter what values are set beyond the returned length.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        placeHolder = {}
        for elements in nums:
            if elements not in placeHolder:
                placeHolder[elements] = 1
            else:
                placeHolder[elements] += 1
        for key in placeHolder:
            if placeHolder[key] > 1:
                to_remove = placeHolder[key] - 1
                for i in range(to_remove):               
                    nums.remove(key)