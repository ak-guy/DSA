# kind of brute force
from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        output = []
        products.sort()  # lexicographically sorting the products array
        n = len(products)

        for ind in range(len(searchWord)):
            search_result = []
            first_matching_product_ind = None
            """
            will use BS to find first occurence of a matching searchWord in products array
            """
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                if products[m][0 : ind + 1] == searchWord[0 : ind + 1]:
                    first_matching_product_ind = m
                    r = m - 1
                elif products[m][0 : ind + 1] > searchWord[0 : ind + 1]:
                    r = m - 1
                else:
                    l = m + 1

            """
            will use the first occurance of matching searchWord's ind and take max three values
            """
            for i in range(3):
                if (
                    first_matching_product_ind is not None
                    and first_matching_product_ind + i < n
                    and products[first_matching_product_ind + i][0 : ind + 1]
                    == searchWord[0 : ind + 1]
                ):
                    search_result.append(products[first_matching_product_ind + i])

            output.append(search_result)

        return output
