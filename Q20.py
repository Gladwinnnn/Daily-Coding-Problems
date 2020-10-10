Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4

Input: nums = [1,3,5,6], target = 0
Output: 0

Input: nums = [1], target = 0
Output: 0

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            lower = 0
            upper = len(nums) - 1
            middle = (upper + lower) // 2
            while lower <= upper:
                if nums[middle] == target:
                    return middle
                elif nums[middle] > target:
                    upper = middle - 1
                elif nums[middle] < target:
                    lower = middle + 1    
                middle = (upper + lower) // 2
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
            return len(nums)
                