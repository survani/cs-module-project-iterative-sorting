def linear_search(arr, target):
    # Your code here

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start_index = 0
    last_index = len(arr) - 1

    while start_index <= last_index:
        middle_i = start_index + (last_index - start_index) // 2
        middle_i_value = arr[middle_i]
        if middle_i_value == target:
            return middle_i

        elif target < middle_i_value:
            last_index = middle_i - 1

        else:
            start_index = middle_i + 1

    return -1  # not found
