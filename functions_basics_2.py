def countdown(num):
    x = num
    newarr = []
    for y in range(num, -1, -1):
        
        newarr.append(x)
        x -= 1
    return newarr
# print(countdown(5))

def prinn(arr):
    print(arr[0])
    return arr[1]

def firstt(arr):
    return (arr[0] + len(arr))

def secc(arr):
    if len(arr) < 2:
        return False
    newarr = []
    x = 0
    while x < len(arr):
        if arr[x] > arr[1]:
            newarr.append(arr[x])
        x += 1
    return newarr


def gfhf(x, y):
    arr = []
    for i in range(x):
        arr.append(y)
    return arr

print(gfhf(6,7))
