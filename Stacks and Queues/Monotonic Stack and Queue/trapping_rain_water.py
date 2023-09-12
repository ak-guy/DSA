# # Method - 1 (Using precomputation for getting maximum height of building to left of index 'i' and to right of index 'i')
class Solution: # TC -> O(N) and SC -> O(N)
    def trappingWater(self, arr,n):
        main_res = 0
        prefix_height = [0 for i in range(n)]
        suffix_height = [0 for i in range(n)]
        
        max_height = arr[0]
        for i in range(n):
            max_height = max(arr[i], max_height)
            prefix_height[i] = max_height
        
        max_height = arr[-1]
        for i in range(n-1, -1, -1):
            max_height = max(arr[i], max_height)
            suffix_height[i] = max_height
        
        for i in range(n): # at any index 'i', the amount of water it can store is => min(max_building_height to the left, max_building_height to the right) - ith_building_height 
            main_res += (min(prefix_height[i], suffix_height[i]) - arr[i])
        
        return main_res
    
# # Method - 2 (Using Two Pointer)
class Solution:
    def trappingWater(self, arr,n):
        main_res = 0
        l, r = 0, n-1
        left_max = 0 # this will tell what is (one of the) max height of building to the left of index i 
        right_max = 0 # this will tell what is (one of the) max height of building to the right of index i
        

        ''' 
        for brute force we were using -> main_res += (min(prefix_height[i], suffix_height[i]) - arr[i])
        but here if we know what which one is minimum max_height_left_building or max_height_right_building
        then we can directly add that result to main_res

        '''
        while l <= r:
            if arr[l] <= arr[r]:
                left_max = max(left_max, arr[l])
                main_res += (left_max - arr[l]) # we add like this in res because we are sure that the max_height of builing on the left will be atleast of length arr[l]
                l += 1
            else:
                right_max = max(right_max, arr[r])
                main_res += (right_max - arr[r]) # we add like this in res because we are sure that the max_height of builing on the right will be greater than arr[r]
                r -= 1
        
        return main_res
