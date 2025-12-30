# # https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab


class Solution:
    def rowWithMax1s(self, arr, n, m):
        res = -1
        start_row = 0
        start_col = m - 1
        while True:
            if start_row == n or start_col == -1:
                return res

            if arr[start_row][start_col] == 1:
                res = start_row
                start_col -= 1
            else:
                start_row += 1
