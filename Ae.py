#Linear search
def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i;
    return -1;


list = [1, 10, 5, 3, 12, 44, 14, 6]
x = 14;
n = len(list);
result = search(list, n, x)
if (result == -1):
    print("Element is not present")
else:
    print("Element is present at index", result);

