#Bubble sort
def bubble_sort(x):
    n = len(x)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]

    print("Sorted:")
    for i in range(len(x)):
        print("%d" % x[i])


x = [1, 10, 5, 3, 12, 44, 14, 6]
bubble_sort(x)

