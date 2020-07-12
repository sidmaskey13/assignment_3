#Quick sort
def partition(x, low, high):
    i = (low - 1)
    pivot = x[high]
    for j in range(low, high):
        if x[j] <= pivot:
            i = i + 1
            x[i], x[j] = x[j], x[i]
    x[i + 1], x[high] = x[high], x[i + 1]
    return (i + 1)


def quickSort(x, low, high):
    if low < high:
        pi = partition(x, low, high)
        quickSort(x, low, pi - 1)
        quickSort(x, pi + 1, high)



x = [1, 10, 5, 3, 12, 44, 14, 6]
n = len(x)
quickSort(x, 0, n - 1)
print("Sorted:")
for i in range(n):
    print("%d" % x[i]),



