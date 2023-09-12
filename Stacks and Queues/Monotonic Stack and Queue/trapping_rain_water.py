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
    
