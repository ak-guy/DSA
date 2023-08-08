'''
this problem we can call it as an extension of "Largest Rectangle in Histogram"
'''
class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = []
        res = 0
        
        for ind, val in enumerate(heights):
            start = ind
            while stack and stack[-1][1] > val:
                start, height = stack.pop()
                area = height * (ind - start)
                res = max(res, area)
            
            stack.append([start, val])
        
        # if all are in inc heights
        for start, height in stack:
            area = height * (len(heights) - start)
            res = max(res, area)
        
        return res

    def maximalRectangle(self, matrix) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = -100000
        height = [0 for i in range(m)]
        
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == '1':
                    height[c] += 1
                else:
                    height[c] = 0
                
            res = max(res, self.largestRectangleArea(height))
        
        return res