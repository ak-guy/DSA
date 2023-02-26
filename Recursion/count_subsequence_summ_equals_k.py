def backtrack(i, arr, n, summ):
    if i == n:
        if summ == k:
            return 1
        return 0
    
    # pick
    summ+=arr[i]
    left = backtrack(i+1, arr, n, summ)

    # not_pick
    summ -= arr[i]
    right = backtrack(i+1, arr, n, summ)

    # return
    return left + right

    
arr = [1,2,1]
k = 40
print(backtrack(0, arr, len(arr), 0))