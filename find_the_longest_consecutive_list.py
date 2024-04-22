new_list = [1, 2, 4, 5, 6, 1, 2, 3, 4, 5, 6]


def find_cons(arr):
    collections = []
    long_arr = []
    n = len(arr)
    for i in range(n):
        if i < n - 1 and arr[i] < arr[i + 1]:
            long_arr.append(arr[i])
        else:
            long_arr.append(arr[i])
            if len(collections) < len(long_arr):
                collections = long_arr
            long_arr = []
    return collections


print(find_consec(arr))
