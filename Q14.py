def merge_sort(dummy):
    if len(dummy) > 1:
        half = len(dummy)//2
        left = merge_sort(dummy[:half])
        right = merge_sort(dummy[half:])
        print(f"left:{left}")
        print(f"right:{right}")
        values = []

        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                values.append(right[0])
                right.pop(0)
            elif right[0] > left[0]:
                values.append(left[0])
                left.pop(0)
        for elements in left:
            values.append(elements)
        for elements in right:
            values.append(elements)
        print(f"values:{values}")
    return dummy

print(merge_sort([41,31,93]))

