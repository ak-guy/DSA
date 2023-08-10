arr = [1,1,1,1,1,1,1,1,1,1,1,2,1,1,1]
target = 2
n = len(arr)
def find_occurence(arr, n, target):
    l, r = 0, n-1
    while l <= r:
        m = (l+r) // 2

        if target == arr[m]:
            return True

        if arr[m] == arr[l] and arr[m] == arr[r]:
            l += 1
            r -= 1
        elif arr[l] <= arr[m]: # from mid to r it is sorted
            if target < arr[m] and arr[l] <= target:
                r = m-1
            else:
                l = m+1
        else: # from l to mid it is sorted
            if target > arr[m] and arr[r] >= target: 
                l = m+1
            else:
                r = m-1 

    return False

print(find_occurence(arr, n, target))