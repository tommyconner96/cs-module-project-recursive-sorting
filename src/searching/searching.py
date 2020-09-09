# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # start = 0
    # end = len(arr) - 1

    if end >= start:

        middle_index = (end + start) // 2
        middle_value = arr[middle_index]

        if target == middle_value:
            return middle_index

        elif target > middle_value:
            return binary_search(arr, target, middle_index + 1, end)
        else:
            return binary_search(arr, target, start, middle_index -1)

    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here
