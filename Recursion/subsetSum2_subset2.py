def backtrack(i, res, curr, arr, n):
    if i == n:
        res.append(curr.copy())
        # print(curr)
        return

    # pick
    curr.append(arr[i])
    backtrack(i + 1, res, curr, arr, n)

    # not_pick
    while True:
        if i < n - 1 and arr[i] == arr[i + 1]:
            i += 1
        else:
            break
    curr.pop()
    backtrack(i + 1, res, curr, arr, n)

    # return
    return res


def backtrack2(i, curr, res, arr, n):
    # we can directly add curr to res because we will be making recursion call only when we get unique subset
    res.append(curr.copy())

    for ind in range(i, n):
        if ind > i and arr[ind] == arr[ind - 1]:
            continue

        curr.append(arr[ind])
        backtrack2(ind + 1, curr, res, arr, n)
        curr.pop()

    return res


arr = [1, 1, 1, 2, 2]
arr.sort()
print(backtrack2(0, [], [], arr, len(arr)))
