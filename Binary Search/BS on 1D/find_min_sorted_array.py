'''
facts:
1. at any point if we found out arr[l] <= arr[r] then res will be min(res, arr[l])
2. if above cond does not satisfy then that means array is not in sorted order
3. now since array is not in sorted order then if arr[l] <= arr[m] then it would mean smallest elem is in right half
'''
arr = [4,5,6,7,0,1,2]
n = len(arr)
def find_min(arr, n):
    l, r = 0, n-1
    res = 1e10
    while l <= r:
        m = (l + r) // 2
        if arr[l] <= arr[r]:
            return min(res, arr[l])
        
        res = min(res, arr[m])
        if arr[m] >= arr[l]:
            l = m+1
        else:
            r = m-1
    return res

print(find_min(arr, n))