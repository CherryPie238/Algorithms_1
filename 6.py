def min_sub_array(nums, target):
    min_len = float('inf')

    left = 0
    cur_sum = 0

    for right in range(len(nums)):
        cur_sum += nums[right]

        while cur_sum >= target:
            window_size = right - left + 1

            if window_size < min_len:
                min_len = window_size

            cur_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0