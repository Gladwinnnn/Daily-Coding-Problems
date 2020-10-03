data = [1,2,3,444,5,6,7,8,9,10]

def binary_search(dummy,target):
    lower = 0
    upper = len(dummy) - 1
    middle = (upper - lower) // 2
    while dummy[middle] != target:
        if dummy[middle] > target:
            lower = middle + 1
            print(lower)
        elif dummy[middle] < target:
            upper = middle - 1
            print(upper)
        middle = (upper - lower) // 2
    return middle

print(binary_search(data,9))