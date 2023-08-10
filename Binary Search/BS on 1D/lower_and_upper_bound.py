def lower_bound(array, target):

    left = 0
    right = len(array) - 1

    if target < array[0]:
        return -1

    while left < right:
        mid = (left + right) // 2

        # In this case only two element will remain
        if left == mid: 
            return left+1 if array[left+1] <= target else left

        # Usual binary search but we know if target is less than mid-value of array then for sure result lies to the left of mid( excluding itself)
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            left = mid
        else:
            right = mid - 1
        
    return left


def upper_bound(array, target):

    left = 0
    right = len(array) - 1

    if target > array[right]:
        return -1

    while left < right:
        mid = (left + right) // 2

        # In this case only two element will remain
        if left == mid: 
            return left if array[left] >= target else left+1

        # Usual binary search but we know if target is greater than mid-value of array then for sure result lies to the right of mid( excluding itself)
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            left = mid + 1
        else:
            right = mid
        
    return left


# Driver Code
target = int(input())
array = [1,2,4,6,10,12,14]
if lower_bound(array, target) == -1:
    print(f"Lower Bound of target {target} is : Does Not Exist")
else:
    print(f"Lower Bound of target {target} is :",array[lower_bound(array, target)])

if upper_bound(array, target) == -1:
    print(f"Upper Bound of target {target} is : Does Not Exist")
else:
    print(f"Lower Bound of target {target} is :",array[upper_bound(array, target)])
