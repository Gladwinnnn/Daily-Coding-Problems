data = "123"

def decode(dummy):
    placeHolder = []
    placeHolder2 = []
    for elements in dummy:
        if int(elements) > 0 or int(elements) < 27:
            placeHolder.append(elements)
    if int(dummy[0:2]) > 0 or int(dummy[0:2]) < 27:
        placeHolder2.append(dummy[0:2])
        temp = dummy[2:]
        for elements in temp:
            if int(elements) > 0 or int(elements) < 27:
                placeHolder2.append(elements)
    return len(placeHolder) + len(placeHolder2)

print(decode(data))