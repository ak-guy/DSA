from typing import List

'''
DFS : 
'''
class Solution:
    def fillColorDFS(self, r, c, image, n, m, color, actual_value) -> None:
        if r < 0 or c < 0 or r >= n or c >= m or image[r][c] != actual_value or image[r][c] == color:
            return

        image[r][c] = color
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        for i in range(4):
            row = r + directions[i][0]
            col = c + directions[i][1]
            self.fillColorDFS(row, col, image, n, m, color, actual_value)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        actual_value = image[sr][sc]
        self.fillColorDFS(sr, sc, image, n, m, color, actual_value)

        return image