def backtrack(i, res, curr, arr, n, summ):
    if i == n:
        if summ == k:
            res.append(curr.copy())
        # print(curr)
        return
    
    # pick
    curr.append(arr[i])
    summ+=arr[i]
    backtrack(i+1, res, curr, arr, n, summ)

    # not_pick
    curr.pop()
    summ -= arr[i]
    backtrack(i+1, res, curr, arr, n, summ)

    # return
    return res

    
arr = [1,2,1]
k = 2
print(backtrack(0, [], [], arr, len(arr), 0))