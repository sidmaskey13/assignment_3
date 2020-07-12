#Insertion sort
def insertion_sort(x):
    for i in range(1, len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key

    print("Sorted:")
    for i in range(len(x)):
        print("%d" % x[i])


x = [1, 10, 5, 3, 12, 44, 14, 6]
insertion_sort(x)
