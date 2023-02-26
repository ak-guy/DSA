def backtrack(i, res, curr, arr, n):
    if i == n:
        res.append(curr.copy())
        # print(curr)
        return
    
    # pick
    curr.append(arr[i])
    backtrack(i+1, res, curr, arr, n)

    # not_pick
    curr.pop()
    backtrack(i+1, res, curr, arr, n)

    # return
    return res

    
arr = [1,2,3]
print(backtrack(0, [], [], arr, len(arr)))