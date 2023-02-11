def peakElement(arr, n):
    left, right = 0, n-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left

array = [1,2,3]
print("Peak element index is ->", peakElement(array, len(array)))
