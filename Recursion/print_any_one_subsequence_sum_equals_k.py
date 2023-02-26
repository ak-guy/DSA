def backtrack(i, res, curr, arr, n, summ):
    if i == n:
        if summ == k:
            print(*curr)
            return True
        # print(curr)
        return False
    
    # pick
    curr.append(arr[i])
    summ += arr[i]
    if backtrack(i+1, res, curr, arr, n, summ): return True

    # not_pick
    curr.pop()
    summ -= arr[i]
    if backtrack(i+1, res, curr, arr, n, summ): return True

    return False

    
arr = [1,2,1]
k = 2
backtrack(0, [], [], arr, len(arr), 0)