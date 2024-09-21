'''
can be solved using either lower bound or upper bound of target value
'''
def searchInsertK(self, Arr, N, k):
    
        # finding upper bound will be all
        def upper_bound(array, target):
            left = 0
            right = len(array) - 1
        
            if target > array[right]:
                return len(array)
            
            if target < array[left]:
                return 0
        
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
            
        return upper_bound(Arr, k)