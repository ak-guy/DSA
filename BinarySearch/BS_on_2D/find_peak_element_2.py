'''
Approach 1 (wrong one) -> go row by row, find peak_element in that row, check its upper and lower element 
                          if the peak_element is greater than both upper and lower element return [row,col]

                          Issue with this approach is when we find peak_element in a row, it is not guaranteed
                          to be the only peak element, but our search for peak_element will stop as soon as we
                          find any peak_element, so we might miss that peak_element which is greater than both
                          upper and lower element

                          Take this example and do dry run -> matrix = [[7,2,3,1,2],[6,5,4,2,1]]
'''
class Solution:
    def findPeakElementInArray(self, arr):
        n = len(arr)
        l, r = 0, n-1
        while l < r:
            mid = (l+r) // 2
            if arr[mid] > arr[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l

    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            ind = self.findPeakElementInArray(mat[i])
            peak_element = mat[i][ind]

            above_element = -1
            if i > 0:
                above_element = mat[i-1][ind]

            below_element = -1
            if i < n-1:
                below_element = mat[i+1][ind]
            
            if peak_element > above_element and peak_element > below_element:
                return [i, ind]
    
'''
Approach - 2 (correct one) -> in this approach we will apply BS to column, then for each col we will find
                              greatest element and then check if it is greater than its left and right or
                              not, using this way we are sure that max of any col will be greater than its
                              upper and lower elements also there wont be any instances of having other 
                              greater element like in previous approach.
'''
class Solution:
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])

        start_col = 0
        end_col = m-1

        while start_col <= end_col:
            mid_col = (start_col + end_col) // 2

            # find row of max element in mid_col
            max_element_row = 0
            for row in range(1, n):
                max_element_row = row if mat[row][mid_col] > mat[max_element_row][mid_col] else max_element_row
                
            left_element = -1
            if mid_col > 0:
                left_element = mat[max_element_row][mid_col-1]

            right_element = -1
            if mid_col < m-1:
                right_element = mat[max_element_row][mid_col+1]
                
            is_greater_than_left = mat[max_element_row][mid_col] > left_element
            is_greater_than_right = mat[max_element_row][mid_col] > right_element

            if is_greater_than_left and is_greater_than_right:
                return [max_element_row, mid_col]
            elif not is_greater_than_right:
                start_col = mid_col + 1
            else:
                end_col = mid_col - 1
        
        return []