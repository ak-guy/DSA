"""
1105. Filling Bookcase Shelves
"""

from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        maxHeight = 0
        for book in books:
            maxHeight += book[1]
        dp = [[-1 for _ in range(shelfWidth + 1)] for _ in range(n + 1)]

        def f(ind, currentSelfMaxHeight, remainingWidth):
            if ind == n:
                dp[ind][remainingWidth] = currentSelfMaxHeight
                return dp[ind][remainingWidth]

            if dp[ind][remainingWidth] != -1:
                return dp[ind][remainingWidth]

            # we are keeping it above our current shelf Number
            differentSelf = currentSelfMaxHeight + f(
                ind + 1,
                currentSelfMaxHeight=books[ind][1],
                remainingWidth=shelfWidth - books[ind][0],
            )

            # keeping book on same shelf
            sameSelf = 1_000_000_000
            if remainingWidth >= books[ind][0]:
                sameSelf = f(
                    ind + 1,
                    currentSelfMaxHeight=max(currentSelfMaxHeight, books[ind][1]),
                    remainingWidth=remainingWidth - books[ind][0],
                )

            dp[ind][remainingWidth] = min(differentSelf, sameSelf)
            return dp[ind][remainingWidth]

        return f(0, 0, shelfWidth)
