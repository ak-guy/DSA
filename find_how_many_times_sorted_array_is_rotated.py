# just return the smallest integer's index (Find minimum in rotated sorted array)
def solve(arr, n):    
    # finding the smallest number
    l, r = 0, n-1
    res = 1e10
    while l <= r:
        m = (l + r) // 2

        if arr[l] <= arr[r]:
            res = min(res, arr[l])
            break
        
        res = min(res, arr[m])
        
        if arr[m] >= arr[l]:
            l = m+1
        else:
            r = m-1

    # finding on which index that smallest number is
    l, r = 0, n-1
    target = res
    while l < r:
        m = (l+r) // 2
        if target == arr[m]:
            return (m,res)
        elif arr[m] <= arr[r]: # from mid to r it is sorted
            if target >= arr[m] and arr[r] >= target:
                l = m+1
            else:
                r = m-1
        else: # from l to mid it is sorted
            if target <= arr[m] and arr[l] <= target:
                r = m-1
            else:
                l = m+1

    return (l,res)

arr = [1,2,3,4,5]
n = len(arr)
print(solve(arr, n))