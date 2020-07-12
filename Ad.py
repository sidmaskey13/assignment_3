#Merge sort
def merge_sort(x):
    if len(x) >1:
        mid = len(x)//2
        L = x[:mid]
        R = x[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                x[k] = L[i]
                i+= 1
            else:
                x[k] = R[j]
                j+= 1
            k+= 1

        while i < len(L):
            x[k] = L[i]
            i+= 1
            k+= 1

        while j < len(R):
            x[k] = R[j]
            j+= 1
            k+= 1


def print_list(x):
    for i in range(len(x)):
        print(x[i], end =" ")
    print()


if __name__ == '__main__':
    x = [1, 10, 5, 3, 12, 44, 14, 6]
    merge_sort(x)
    print("Sorted: ", end ="\n")
    print_list(x)