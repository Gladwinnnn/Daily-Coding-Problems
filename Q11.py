data = [1,2,3,4,5,6,7,8,9,10]

def binary_search(dummy,target):
    lower = 0
    upper = len(dummy) - 1
    middle = (upper + lower) // 2
    while lower < upper:
        if dummy[middle] == target:
            return middle
        elif dummy[middle] > target:
            upper = middle - 1
        elif dummy[middle] < target:
            lower = middle + 1    
        middle = (upper + lower) // 2
    return -1

print(binary_search(data,9))