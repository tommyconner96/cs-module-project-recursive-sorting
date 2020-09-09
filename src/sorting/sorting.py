# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # index points for arrays when it loops thru
    index_a = 0
    index_b = 0
    index_merged = 0

    while index_a < len(arrA) and index_b < len(arrB):
        if arrA[index_a] < arrB[index_b]:
            merged_arr[index_merged] = arrA[index_a]
            index_a +=1
        else:
            merged_arr[index_merged] = arrB[index_b]
            index_b +=1

        index_merged +=1

    while index_a < len(arrA):
        merged_arr[index_merged] = arrA[index_a]
        index_a += 1
        index_merged +=1

    while index_b < len(arrB):
        merged_arr[index_merged] = arrB[index_b]
        index_b +=1
        index_merged +=1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        midpoint = len(arr) // 2
        left = merge_sort(arr[:midpoint])
        right = merge_sort(arr[midpoint:])

        return merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

