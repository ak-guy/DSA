"""
same as search in sorted rotated array 1 but we need to handle duplicate values,
duplicate will create issue when we cannot know which side is sorted we can take example of
arr =[1,1,1,1,1,1,1,1,1,1,1,2,1,1,1]
in this, for first iteration we cannot know which side is sorted, so to handle such case
we can checking if arr[l] == arr[m] and arr[m] == arr[r] then we will move l+=1 and r-=1
"""

arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1]
target = 2
n = len(arr)


def find_occurence(arr, n, target):
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2

        if target == arr[m]:
            return True

        if arr[m] == arr[l] and arr[m] == arr[r]:
            l += 1
            r -= 1
        elif arr[l] <= arr[m]:  # from mid to r it is sorted
            if target < arr[m] and arr[l] <= target:
                r = m - 1
            else:
                l = m + 1
        else:  # from l to mid it is sorted
            if target > arr[m] and arr[r] >= target:
                l = m + 1
            else:
                r = m - 1

    return False


print(find_occurence(arr, n, target))
