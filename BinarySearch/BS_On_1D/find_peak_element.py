"""
peak element, arr[i], is an element such that arr[i-1] < arr[i] > arr[i+1]
every array will always have atleast one peak element
suppose we have an index m = 5, then we check arr[5] > arr[6] if this condition is true then
it means arr[5] can be a peak element so we will shift right_pointer to index 5 else left_pointer to 6
"""


def peakElement(arr, n):
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


array = [1, 2, 3]
print("Peak element index is ->", peakElement(array, len(array)))
