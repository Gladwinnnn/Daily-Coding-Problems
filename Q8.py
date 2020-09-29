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