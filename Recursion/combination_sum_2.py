def backtrack(i, arr, curr, res, n, target, currsumm):
    if currsumm > target:
        return
    
    if currsumm == target:
        res.append(curr.copy())
        return
    
    for ind in range(i, n):
        
        if ind > i and arr[ind] == arr[ind-1]:
            continue

        if arr[ind] > target:
            break

        currsumm += arr[ind]
        curr.append(arr[ind])
        backtrack(ind+1, arr, curr, res, n ,target, currsumm) # to get combination_sum_1 -> just make function call for ind and not for ind+1 

        currsumm -= arr[ind]
        curr.pop()

    return res

arr = [4, 19, 30, 11]
arr.sort()
target = 30

print(backtrack(0, arr, [], [], len(arr), target, 0))