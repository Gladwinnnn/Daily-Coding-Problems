# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Follow up: The overall run time complexity should be O(log (m+n)).

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000

# Input: nums1 = [2], nums2 = []
# Output: 2.00000

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for elements in nums2:
            nums1.append(elements)
    
        sorted_list = merge_sort(nums1)
        
        if len(sorted_list) % 2 != 0:
            return float(sorted_list[len(sorted_list)//2])
        else:
            return float((sorted_list[len(sorted_list)//2]+sorted_list[len(sorted_list)//2-1])/2)
    
def merge_sort(dummy):
    if len(dummy) > 1:
        half = len(dummy)//2
        left = merge_sort(dummy[:half])
        right = merge_sort(dummy[half:])
        values = []

        while len(left) > 0 and len(right) > 0:
            if left[0] >= right[0]:
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