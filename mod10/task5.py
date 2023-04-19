def find_insert_position(arr, x):
    if (len(arr) == 0):
        return 0
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return left


A = [1, 2, 3, 3, 3, 5]
x = 4
print(find_insert_position(A, x))
