# # Leetcode
class Solution:
    '''
    idea is to move in reverse on nums2 and maintain a monotonic inc stack
    '''
    def nextGreaterElement(self, nums1, nums2):
        st = [] # this will be our monotonically increasing stack, st[-1] < st[-2]
        hmap = {val:ind for ind, val in enumerate(nums1)}

        # instead of creating a new result array, will modify nums1
        for i in range(len(nums2)-1, -1, -1):
            val = nums2[i]
            while st and st[-1] < val: # to keep the stack monotonically increasing we will keep poping st[-1] > val
                st.pop()

            if val in hmap:
                if not st: # if stack is empty and val exists in hmap
                    nums1[hmap[val]] = -1
                else: # if stack is not empty and val exist in hmap
                    res = st.pop() # no st.top() or st.peek() exist, so need to pop to get the value, but will add this later to stack
                    nums1[hmap[val]] = res
                    st.append(res) # adding to stack the poped value

            st.append(val)
        
        return nums1
    

# # GFG
class Solution:
    def nextLargerElement(self,nums2,n):
        nums1 = [-1 for i in range(n)] 
        st = [] # this will be our monotonically increasing stack, st[-1] < st[-2]
        
        for i in range(len(nums2)-1, -1, -1):
            val = nums2[i]
            while st and st[-1] <= val:
                st.pop()
            
            if st:
                res = st.pop()
                nums1[i] = res
                st.append(res)
                
            st.append(val)
        
        return nums1