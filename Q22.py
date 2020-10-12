# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Given nums = [3,2,2,3], val = 3,

# Your function should return length = 2, with the first two elements of nums being 2.

# It doesn't matter what you leave beyond the returned length.

# Given nums = [0,1,2,2,3,0,4,2], val = 2,

# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

# Note that the order of those five elements can be arbitrary.

# It doesn't matter what values are set beyond the returned length.

def merge_sort(dummy,val):
    if len(dummy) == 1:
        if dummy[0] == val:
            dummy.pop(0)
        print(dummy)
        return dummy[:1]
    else:
        return merge_sort(dummy[:1],val) + merge_sort(dummy[1:],val) 
print(merge_sort([0,1,2,2,3,0,4,2],2))