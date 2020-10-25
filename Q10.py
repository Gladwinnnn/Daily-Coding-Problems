data = "123"

def decode(dummy):
    placeHolder = []
    placeHolder2 = []
    for elements in dummy:
        if int(elements) > 0 and int(elements) < 27:
            placeHolder.append(elements)
    print(placeHolder)
    if int(dummy[0:2]) > 0 and int(dummy[0:2]) < 27:
        placeHolder2.append(dummy[0:2])
        temp = dummy[2:]
        for elements in temp:
            if int(elements) > 0 and int(elements) < 27:
                placeHolder2.append(elements)
    return len(placeHolder) + len(placeHolder2)

print(decode(data))
print(decode("226"))