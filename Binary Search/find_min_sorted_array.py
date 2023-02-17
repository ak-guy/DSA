arr = [4,5,6,7,0,1,2]
n = len(arr)
def find_min(arr, n):
    l, r = 0, n-1
    res = 1e10

    while l <= r:
        m = (l + r) // 2

        # if we found left to right sorted array
        if arr[l] <= arr[r]:
            return min(res, arr[l])
        
        res = min(res, arr[m])
        if arr[m] >= arr[l]: # for this case min could be at left(already took care of it) or to the left side of mid
            l = m+1
        else:
            r = m-1# in case of no rotation
    if arr[l] <= arr[r]:
        return arr[0]

    return res

print(find_min(arr, n))