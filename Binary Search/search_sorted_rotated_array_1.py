# rotated_sorted_arr = sorted_arr + sorted_arr    ----> meaning it can be divided into two sorted arrays
# if arr[l] <= arr[mid] this means from l to mid it is sorted
# or if arr[mid] <= arr[r] this means from mid to r it is sorted


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
n = len(arr)
def modified_binary_search(arr, n):
    l, r = 0, n-1
    while l < r:
        m = (l+r) // 2
        if target == arr[m]:
            return m
        elif arr[m] <= arr[r]: # from mid to r it is sorted
            if target >= arr[m] and arr[r] >= target:
                l = m+1
            else:
                r = m-1
        else:
            if target <= arr[m] and arr[l] <= target:
                r = m-1
            else:
                l = m+1
    return l

for i in range(1, 11):
    target = i
    print(str(i) + " --> " + str(modified_binary_search(arr, n)))