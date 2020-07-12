#Interpolation Search
def interpolation_search(list, n, x):
    lo = 0
    hi = (n - 1)

    while lo <= hi and x >= list[lo] and x <= list[hi]:
        if lo == hi:
            if list[lo] == x:
                return lo
            return -1
        pos = lo + int(((float(hi - lo) /
                         (list[hi] - list[lo])) * (x - list[lo])))
        if list[pos] == x:
            return pos
        if list[pos] < x:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1


LIST = [1, 4, 9, 10, 14, 19, 44]
n = len(LIST)

x = 14
index = interpolation_search(LIST, n, x)

if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
