def reverse_array(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1


def solution(arr, k):
    n = len(arr)
    k = k % n

    reverse_array(arr, 0, n - 1)
    reverse_array(arr, 0, k - 1)
    reverse_array(arr, k, n - 1)

    return arr