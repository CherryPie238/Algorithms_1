def move_zeroes(arr):
    non_zero_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[non_zero_index] = arr[non_zero_index], arr[i]
            non_zero_index += 1

    return arr