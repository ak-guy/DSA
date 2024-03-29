# # Help Classmate (GFG)
class Solution:
    '''
    similar to next greater element, only difference is we will maintain a mono dec stack here
    '''
    def help_classmate(self, nums2, n):
        nums1 = [-1 for i in range(n)] 
        st = [] # this will be our monotonically decreasing stack, st[-1] > st[-2]
        
        for i in range(n-1, -1, -1):
            val = nums2[i]
            while st and st[-1] >= val:
                st.pop()
            
            if st:
                res = st.pop()
                nums1[i] = res
                st.append(res)
                
            st.append(val)
        
        return nums1