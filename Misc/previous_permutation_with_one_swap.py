# similar concept as Next permutation
class Solution: # # Leetcode (previous permutation with one swap)
    def prevPermOpt1(self, arr):
        n = len(arr)
        bp = -1
        for i in range(n-2, -1, -1):
            if arr[i+1] < arr[i]:
                bp = i
                break
            
        if bp == -1:
            return arr

        res_ind = -1
        for i in range(n-1, bp-1, -1):
            if arr[bp] > arr[i] and (i>0 and arr[i] != arr[i-1]): # this cond -> (i>0 and arr[i] != arr[i-1]) is because there can exist duplicate, so we will pick last duplicate elem present if we start traversing from back  
                arr[bp], arr[i] = arr[i], arr[bp]
                break

        return arr
    

class Solution: # # GFG (Previous number in one swap)
    def previousNumber (ob,S):
        arr = [int(i) for i in S]
        n = len(arr)
        bp = -1
        for i in range(n-2, -1, -1):
            if arr[i+1] < arr[i]:
                bp = i
                break
            
        if bp == -1:
            return "-1"

        res_ind = -1
        for i in range(n-1, bp-1, -1):
            if arr[bp] > arr[i] and (i>0 and arr[i] != arr[i-1]): # this cond -> (i>0 and arr[i] != arr[i-1]) is because there can exist duplicate, so we will pick last duplicate elem present if we start traversing from back  
                arr[bp], arr[i] = arr[i], arr[bp]
                break
            
        res = "".join(str(val) for val in arr)
        if res[0] == '0':
            return "-1"
        else:
            return res