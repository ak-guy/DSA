arr = [-10, 5, 2, -23, 3]


def merge(arr, l, mid, r):
    L = arr[l : mid + 1]
    R = arr[mid + 1 : r + 1]

    startL, endL = 0, len(L)
    startR, endR = 0, len(R)
    resPointer = l
    while startL < endL and startR < endR:
        if L[startL] < R[startR]:
            arr[resPointer] = L[startL]
            startL += 1
        else:
            arr[resPointer] = R[startR]
            startR += 1
        resPointer += 1

    while startL < endL:
        arr[resPointer] = L[startL]
        resPointer += 1
        startL += 1

    while startR < endR:
        arr[resPointer] = R[startR]
        resPointer += 1
        startR += 1


def mergeSort(arr, l=0, r=len(arr) - 1):
    if l < r:
        mid = (l + r) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)
        merge(arr, l, mid, r)


mergeSort(arr)
print(arr)
